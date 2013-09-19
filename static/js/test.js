(function() {
  $('#set_bg').click(function() {
    return $.cookie.set({
      'bg_url': url
    }, 999, "/");
  });

  $('#clear_bg').click(function() {
    return $.cookie.set({
      'bg_url': null
    }, 999, "/");
  });

  $('#search').click(function() {
    var q;

    q = $('#q').val();
    return location.href('/search?q=' + q);
  });

}).call(this);
