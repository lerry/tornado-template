$('#set_bg').click ->
    $.cookie.set({'bg_url':url}, 999, "/")
$('#clear_bg').click ->
    $.cookie.set({'bg_url': null}, 999, "/")

$('#search').click ->
    q = $('#q').val()
    location.href('/search?q='+q)