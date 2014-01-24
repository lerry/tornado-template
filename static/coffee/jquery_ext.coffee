$(document).ajaxError (event, request, settings) ->
    status = request.status
    if status and status!=200
        alert("出错 : #{status}\n#{settings.url}")

jQuery.fn.extend(
    yellow_fade :(t=500) ->
        _ = $(@)
        _.css({backgroundColor: "#ffffcc"}).animate(
            {
                    backgroundColor: "#ffffff"
            }, t, 
            ->
                _.css({backgroundColor:''}) 
        )
        return _
    font_fade : (o='red',t=500)->
        _ = $(@)
        _.css({color:o}).animate(
            {
                    backgroundColor: "#ffffff"
            }, t, 
            ->
                _.css({color:'black'}) 
        )
        return _

    ctrl_enter : (callback) ->
        $(this).keydown(
            (event) ->
                event = event.originalEvent
                if event.keyCode == 13 and (event.metaKey or event.ctrlKey)
                    callback?()
                    false
        )

    click_drop : (drop, callback1, callback2) ->
        html = $("html,body")
        $(@).click (e)->
            self = @
            self.blur()
            
            _ = ->
                drop.hide()
                html.unbind 'click' , _
                callback2 and callback2()
            if drop.is(":hidden")
                drop.show()
                e.stopPropagation()
                html.click(_)
                clicked = true
                callback1 and callback1()
            else
                _()
    
    just_number : (d) ->
        ni = $(@)
        if d==undefined or isNaN d or d<0
            d=8
        re = eval("/\\d*\\.?\\d{0," + d + "}/")
        ni.keyup ->
            if isNaN ni.val()
                ni.addClass('num_err')
                ret = re.exec(ni.val())
                if ret
                    ni.val(ret[0])
                else
                    ni.val(0)
                ni.removeClass('num_err')
            else
                ret = re.exec(ni.val())
                if ret and ret[0] != ni.val()
                    ni.val(ret[0])
            return
)

jQuery.extend(

#   js : (url, callback, params...)->
#       fancybox = $.fancybox 
#       fancybox.showLoading()
#       require(
#           [
#               url 
#           ]
#           ->
#               fancybox.hideLoading()
#               if callback
#                   callback = callback.split(".")
#                   t = window
#                   for i in callback
#                       t = t[i]
#                   t.apply(t,params)
#       )


    escape : (txt) -> $('<div/>').text(txt).html()
    html : ->
        # _ = $.html()
        # _ "TEST #{$.escape o.txt}"
        # div.html _.html()
        
        r = []
        _ = (o) -> r.push o
        _.html = -> r.join ''
        _
    uid : ->
         (""+ Math.random()).slice(2)

    postJSON : (url, data, callback) ->
        if jQuery.isFunction data 
            callback = data
            data = 0
        data = data||{}

        _xsrf = $.cookie.get("_xsrf")
        if typeof data=="string"
            data+="&_xsrf="+_xsrf
        else
            data._xsrf = _xsrf
        #console.log url, data, callback 
        return jQuery.ajax(
            url: url,
            data: data,
            dataType: "json",
            type: "POST",
            success: _ajax_success(callback)
        )

    # error = Err("password",) error.xxx.set
    #
    isotime : (timestamp) ->
      date = new Date(timestamp * 1000)
      hour = date.getHours()
      minute = date.getMinutes()
      hour = "0" + hour  if hour < 9
      minute = "0" + minute  if minute < 9
      result = [date.getMonth() + 1, date.getDate()]
      now = new Date()
      full_year = date.getFullYear()
      result.unshift full_year  unless now.getFullYear() is full_year
      result.join("-") + " " + [hour, minute].join(":")

    timeago : (timestamp) ->
      date = new Date(timestamp * 1000)
      ago = parseInt((new Date().getTime() - date.getTime()) / 1000)
      minute = undefined
      if ago <= 0
        return "刚刚"
      else if ago < 60
        return ago + "秒前"
      else
        minute = parseInt(ago / 60)
        return minute + "分钟前"  if minute < 60
      jQuery.isotime(timestamp).split(" ")[0]

    num_format : (num, length) ->
        num = num - 0
        if num < 0.01
            length = 8
        if length
            num = num.toFixed(length)
        return num - 0

    errtip : (o) ->
        elem = $(o)
        if elem[0].tagName == "FORM"
            elem.find("input:first").focus()
            kv = []
            return {
                reset : (o) ->
                    for v in kv
                        v.reset()
                    kv = []

                set : (o) ->
                    @reset()

                    if typeof(o) == "string"
                        alert o
                        return 1 
                    focused = 0
                    count = 0
                    for k, v of o
                        count += 1
                        t = elem.find("[name=#{k}]")
                        if not t[0]
                            alert v
                            continue
                        if not focused and t[0].tagName == "INPUT"
                            t.focus().select()
                            focused = 1
                        tip = t.nextAll('.tip')
                        if tip.length
                            t = $.errtip tip 
                            t.set(v)
                            kv.push t 
                        else
                            alert v
                    return count 
            }

        else
            html = elem.data('default')

            if not html
                html = elem.html()
                elem.data('default', html)

            return {
                set : (content)->
                    @reset()
                    if content
                        elem.addClass("err").html(content).fadeOut().fadeIn()
                        return 1
                    return 0 
                reset : ->
                    elem.html(html).removeClass("err")
            }
         
)
_ajax_success = (callback) ->
    _ = (data, textStatus, jqXHR) ->
        if data and data.error
            error = data.error
            if error.code == 403
                return $$("SSO.login")
            else if error.html
                $.is_posting = 0 
                return $.fancybox({content:error.html})

        if callback
            callback(data, textStatus, jqXHR)
    return _

jQuery.getJSON = ( url , data , callback ) ->
    if jQuery.isFunction data 
        callback = data
        data = 0
    return jQuery.ajax(
        url: url,
        cache: false,
        data: data||{},
        dataType: "json",
        type: "GET",
        success: _ajax_success(callback)
    )
    
jQuery.islogin = ->
    user_id = $.cookie.get("U")
    if user_id
        return user_id - 0
    return 0


$.whenScroll = (pos, callback) ->
    win = $ window
    top = win.scrollTop()

    win.scroll ->
        _top = win.scrollTop()

        _ = ( top <= pos and _top > pos  ) or ( top >= pos and _top < pos ) 
        top = _top
        if _
            callback(_top)

    if top > pos
        callback(top)


ajaxing = ( func) ->
    return (url, data, callback) ->
        if $.is_posting
            return 
        $.is_posting = 1
        if jQuery.isFunction data 
            callback = data
            data = 0
        fancybox = $.fancybox
        fancybox.showLoading()
        end = ->
            fancybox.hideLoading()
            $.is_posting = 0
        func(
            url, data, 
            (data, textStatus, jqXHR) ->
                fancybox.hideLoading()
                $.is_posting = 0
                callback(data, textStatus, jqXHR)
                end()
        ).error(end)

$.postJSON1 = ajaxing($.postJSON)
$.getJSON1 = ajaxing($.getJSON)
$.get1 = ajaxing($.get)
$.post1 = ajaxing($.post)






 
