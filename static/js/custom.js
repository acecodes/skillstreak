$(document).ready(function() {

        var refresh = function() {
            $(".streaks").load(" .single_streak");
        };


            // Fade in effect for streak boxes
            $(".streak_box").hide().fadeIn(450);

            var csrftoken = $.cookie('csrftoken');

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
                        "activity": "AJAX17 testing",
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
                })
                    .success(function(r) {
                        refresh();
                        console.log("success", r);
                    });
            });

            $(".delete_button").click(function() {
                var id = "{{ i.id }}";
                $.ajax({
                    type: "DELETE",
                    url: '/api/streaks/' + id,
                    contentType: 'application/json',
                    dataType: 'json',
                    data: JSON.stringify({
                        "id": 31,
                        "csrfmiddlewaretoken": csrftoken
                    })

                }).error(function(r) {
                    console.log(r);
                })
                    .success(function(r) {
                        refresh();
                        console.log("success", r);
                    });
            });

            // Button to test AJAX refresh
            $(".refresh_button").click(function() {
                refresh();
            });
        });