(function() {
    'use strict';

    /**
     * @ngdoc function
     * @name streakApp.controller:StreakCtrl
     * @description
     * # StreakCtrl
     * Controller of the frontendApp
     */
    angular.module('streakApp')
        .controller('StreakCtrl', function($scope, djResource) {

            // Get streaks for user
            var Streak = djResource('/api/streaks/:streakId', {
                streakId: '@id'
            });

            $scope.streak = Streak.query();

            // Get user info and use it for making new streaks
            var User = djResource('/api/users/:userId', {
                userId: '@id'
            });
            var userInfo = User.query(function() {
                var user = userInfo[0];
                var userName = user.username;
                $scope.newStreak = new Streak({
                    'user': userName
                });
            });


        })
        .controller('FormCtrl', function($scope, djResource) {
            $scope.addStreak = function(activity) {
                $scope.streak = angular.copy(activity);
                activity.$save();
            };
        });
})();