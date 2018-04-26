"use strict";

$(function(){
    const $ = window.$;
    $.meta = function(name){
        return $("meta[name=" + name + "]").attr('content');
    };

    let hhcms = {};
    window.hhcms = hhcms;

    hhcms.csrf_token = $("meta[name=CSRF_TOKEN]").attr('content');

    // init the whole page popover
    $('[data-toggle="popover"]').popover();

    hhcms.user_exists = function(username, email, success_callback, error_callback)
    {
        let payload = {
            'username': username,
            'email': email
        };

        let url = $.meta('USER_EXISTS_URL');

        $.ajax({
            'headers': {"X-CSRFToken": hhcms.csrf_token},
            'url': url,
            'type': 'POST',
            'data': payload,
            'success': success_callback,
            'error': error_callback
        });

    };
});

