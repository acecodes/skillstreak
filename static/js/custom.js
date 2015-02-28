$(document).ready(function() {

    // Fade number to be recycled
    var fade = 650;

    // Refresh function for all operations
    var refresh = function() {
        $(".streaks").load(" .single_streak").hide().fadeIn(fade);
    };

    // Show account options
    $("#account_options").click(function() {
        $("#dash_options").fadeIn(fade);
    });

    // Hide account options
    $("#account_options_hide").click(function () {
        $("#dash_options").fadeOut(fade);
    });


    // Fade in effect for streak boxes
    $(".streak_box").hide().fadeIn(fade);


    // CSRF cookie
    var csrftoken = $.cookie('csrftoken');


    // CSRF function that allows AJAX to make API queries
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Button to test AJAX posting
    $(".post_button").click(function() {

        $.ajax({
            type: "POST",
            url: '/api/streaks/',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                "user": "root",
                "activity": "AJAX1 testing",
                "start": "2015-02-21T22:53:51Z",
                "current_streak": 2,
                "longest_streak": 5,
                "resets": 0,
                "last_reset": "2015-02-25T22:53:55Z",
                "notes": "A",
                "csrfmiddlewaretoken": csrftoken
            })

        }).error(function(r) {
            console.log(r);
            $("#error").append(JSON.stringify(r)).fadeIn(fade);
        })
            .success(function(r) {
                refresh();
                console.log("success", r);
            });
    });


    // Button for deleting entries
    $(".delete_button").click(function() {
        // TO-DO: Create delete button
        console.log("Nothing here yet!");
    });

    // Button to test AJAX refresh
    $(".refresh_button").click(function() {
        refresh();
    });
});