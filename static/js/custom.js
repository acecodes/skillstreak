$(document).ready(function() {
    // Fade in effect for streak boxes
    $(".streak_box").hide().fadeIn(450);

    // Button to test AJAX posting
    $(".test_button").click(function() {
        $.ajax({
            type: "POST",
            url: '/api/streaks/',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                "user": "root",
                "activity": "AJAX test",
                "start": "2015-02-27T22:53:51Z",
                "current_streak": 2,
                "longest_streak": 5,
                "resets": 0,
                "last_reset": "2015-02-25T22:53:55Z",
                "notes": "A"
            })
            
        }).error(function(r){ console.log(r); })
.success(function(r){ console.log("success", r); });
    });
});