(function() {
  var _ajax_success;

  $(document).ajaxError(function(event, request, settings) {
    var status;

    status = request.status;
    if (status && status !== 200) {
      return alert("出错 : " + status + "\n" + settings.url);
    }
  });

  jQuery.fn.extend({
    ctrl_enter: function(callback) {
      return $(this).keydown(function(event) {
        event = event.originalEvent;
        if (event.keyCode === 13 && (event.metaKey || event.ctrlKey)) {
          if (typeof callback === "function") {
            callback();
          }
          return false;
        }
      });
    },
    click_drop: function(drop, callback1, callback2) {
      var html;

      html = $("html,body");
      return $(this).click(function(e) {
        var clicked, self, _;

        self = this;
        self.blur();
        _ = function() {
          drop.hide();
          html.unbind('click', _);
          return callback2 && callback2();
        };
        if (drop.is(":hidden")) {
          drop.show();
          e.stopPropagation();
          html.click(_);
          clicked = true;
          return callback1 && callback1();
        } else {
          return _();
        }
      });
    }
  });

  jQuery.extend({
    escape: function(txt) {
      return $('<div/>').text(txt).html();
    },
    html: function() {
      var r, _;

      r = [];
      _ = function(o) {
        return r.push(o);
      };
      _.html = function() {
        return r.join('');
      };
      return _;
    },
    uid: function() {
      return ("" + Math.random()).slice(2);
    },
    postJSON: function(url, data, callback) {
      var _xsrf;

      if (jQuery.isFunction(data)) {
        callback = data;
        data = 0;
      }
      data = data || {};
      _xsrf = $.cookie.get("_xsrf");
      if (typeof data === "string") {
        data += "&_xsrf=" + _xsrf;
      } else {
        data._xsrf = _xsrf;
      }
      return jQuery.ajax({
        url: url,
        data: data,
        dataType: "json",
        type: "POST",
        success: _ajax_success(callback)
      });
    },
    errtip: function(o) {
      var elem, html, kv;

      elem = $(o);
      if (elem[0].tagName === "FORM") {
        elem.find("input:first").focus();
        kv = [];
        return {
          reset: function(o) {
            var v, _i, _len;

            for (_i = 0, _len = kv.length; _i < _len; _i++) {
              v = kv[_i];
              v.reset();
            }
            return kv = [];
          },
          set: function(o) {
            var count, focused, k, t, tip, v;

            this.reset();
            if (typeof o === "string") {
              alert(o);
              return 1;
            }
            focused = 0;
            count = 0;
            for (k in o) {
              v = o[k];
              count += 1;
              t = elem.find("[name=" + k + "]");
              if (!t[0]) {
                alert(v);
                continue;
              }
              if (!focused && t[0].tagName === "INPUT") {
                t.focus().select();
                focused = 1;
              }
              tip = t.nextAll('.tip');
              if (tip.length) {
                t = $.errtip(tip);
                t.set(v);
                kv.push(t);
              } else {
                alert(v);
              }
            }
            return count;
          }
        };
      } else {
        html = elem.data('default');
        if (!html) {
          html = elem.html();
          elem.data('default', html);
        }
        return {
          set: function(content) {
            return elem.addClass("err").html(content).fadeOut().fadeIn();
          },
          reset: function() {
            return elem.html(html).removeClass("err");
          }
        };
      }
    }
  });

  _ajax_success = function(callback) {
    var _;

    _ = function(data, textStatus, jqXHR) {
      var error;

      if (data && data.error) {
        error = data.error;
        if (error.code === 403) {
          return $$("SSO.login");
        } else if (error.html) {
          return $.fancybox({
            content: error.html
          });
        }
      }
      if (callback) {
        return callback(data, textStatus, jqXHR);
      }
    };
    return _;
  };

  jQuery.getJSON = function(url, data, callback) {
    if (jQuery.isFunction(data)) {
      callback = data;
      data = 0;
    }
    return jQuery.ajax({
      url: url,
      cache: false,
      data: data || {},
      dataType: "json",
      type: "GET",
      success: _ajax_success(callback)
    });
  };

}).call(this);
