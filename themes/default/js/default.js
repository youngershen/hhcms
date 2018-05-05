"use strict";

$(function () {
    const $ = window.$;
    const handlerbars = window.Handlebars;
    $.meta = function (name) {
        return $("meta[name=" + name + "]").attr('content');
    };

    let hhcms = {};

    window.hhcms = hhcms;

    hhcms.csrf_token = $.meta('CSRF_TOKEN');

    $('[data-toggle="popover"]').popover();

    hhcms.user_exists = function (username, email, success_callback, error_callback) {
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


    $('#username').blur(function () {
        $('.warning').remove();

        let username = $('#username').val();
        let source = document.getElementById("username-template").innerHTML;
        let template = handlerbars.compile(source);

        if (!username) {
            let context = {message: "username is required"};
            let html = template(context);
            $(html).insertAfter('#username-row')
        }
        else {
            hhcms.user_exists(username, null, function (data) {
                if (data.status) {
                    let context = {message: "username already exists"};
                    let html = template(context);
                    $(html).insertAfter('#username-row')
                }
            });
        }
    });
});

