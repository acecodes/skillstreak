$(document).ready(function() {
    // Fade in effect for streak boxes
    $(".streak_box").hide().fadeIn(450);

    $(".test_button").click(function() {
        $.ajax({
            url: '/api/streaks/',
            contentType: 'application/json',
            dataType: 'json',
            data: {
                "user": "root2",
                "activity": "Nope ya batch",
                "start": "2015-02-25T22:53:51Z",
                "current_streak": 5,
                "longest_streak": 5,
                "resets": 0,
                "last_reset": "2015-02-25T22:53:55Z",
                "notes": "A"
            },
            
        }).error(function(r){ console.log(r); })
.success(function(r){ console.log("success", r); });
    });
});