$(document).ready(function() {

    // Fade number to be recycled
    var fade = 650;

    // Refresh function for all operations
    var refresh = function() {
        $('.streaks').load(' .single_streak').hide().fadeIn(fade);
    };

    // Show account options
    $('#account_options').click(function() {
        $('#dash_options').fadeIn(fade);
    });

    // Hide account options
    $('#account_options_hide').click(function() {
        $('#dash_options').fadeOut(fade);
    });

    // Show streak adding form
    $('#add_streak').click(function() {
        $('#add_form').fadeIn(fade);
    });

    // Hide streak adding form
    $('#add_form_hide').click(function() {
        $('#add_form').fadeOut(fade);
    });


    // Fade in effect for streak boxes
    $('.streak_box').hide().fadeIn(fade);


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
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });

    // Button to test AJAX posting
    $('.post_button').click(function() {

        $.ajax({
            type: 'POST',
            url: '/api/streaks/',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                'user': 'root',
                'activity': 'AJAX1 testing',
                'start': '2015-02-21T22:53:51Z',
                'current_streak': 2,
                'longest_streak': 5,
                'resets': 0,
                'last_reset': '2015-02-25T22:53:55Z',
                'notes': 'A',
                'csrfmiddlewaretoken': csrftoken
            })

        }).error(function(r) {
            console.log(r);
            $('#error').append(JSON.stringify(r)).fadeIn(fade);
        })
            .success(function(r) {
                refresh();
                console.log('success', r);
            });
    });


    // Button for increasing the streak
    $('.increase_button').click(function() {
        var id = $(this).parent().attr('id').slice(7);
        var curr_streak_id = '#current_streak_' + id;
        var current_streak = Number($(this).parent().contents(curr_streak_id).html());
        var longest_streak_id = '#longest_streak_' + id;
        var longest_streak = Number($(this).parent().contents(longest_streak_id).html());
        var new_streak = current_streak + 1;
        console.log(current_streak, new_streak);
        console.log(longest_streak);

        if (new_streak > longest_streak) {
            longest_streak = new_streak;
        } else {
            longest_streak = longest_streak;
        }

        $.ajax({
            type: 'PATCH',
            url: '/api/streaks/' + id + '/',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                'id': id,
                'current_streak': new_streak,
                'longest_streak': longest_streak,
                'csrfmiddlewaretoken': csrftoken
            })

        }).error(function(r) {
            console.log(r);
            $('#error').append(JSON.stringify(r)).fadeIn(fade);
        })
            .success(function(r) {
                refresh();
                console.log('success', r);
            });
    });


    // Button for deleting entries
    $('.delete_button').click(function() {

        var id = $(this).parent().attr('id').slice(7);

        $.ajax({
            type: 'DELETE',
            url: '/api/streaks/' + id,
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                'id': id,
                'csrfmiddlewaretoken': csrftoken
            })

        }).error(function(r) {
            console.log(r);
            $('#error').append(JSON.stringify(r)).fadeIn(fade);
        })
            .success(function(r) {
                refresh();
                console.log('success', r);
            });
    });

    // Button to test AJAX refresh
    $('.refresh_button').click(function() {
        refresh();
    });

    // Button to test retrieval of streak ID
    $('.id_test').click(function() {
        var id = $(this).parent().attr('id').slice(7);
        console.log(id);
    });
})();