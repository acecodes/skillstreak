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
        .controller('StreakController', function($scope, djResource) {

            // Get streaks for user
            var Streak = djResource('/api/streaks/:streakId', {
                streakId: '@id'
            });

            $scope.streaks = Streak.query();

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

            $scope.deleteStreak = function(index) {
                var indexOfActivity = $scope.streaks[index];
                $scope.streaks.splice(index, 1);
                indexOfActivity.$delete();
            };

            $scope.addStreak = function(activity) {
                $scope.streaks.push(activity);
                activity.$save();
                $scope.newStreak = {};

            };


        })
        .controller('FormController', function($scope, djResource) {

        });
})();