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
      .controller('StreakCtrl', function ($scope, djResource) {
        var Streak = djResource('/api/streaks/:streakId', {streakId:'@id'});
        var User = djResource('/api/users/:userId', {userId:'@id'});
        var userInfo = User.query(function () {
            var user = userInfo[0];
            var userName = user.username;
            $scope.newStreak = new Streak({'user':userName});
        });
        $scope.streak = Streak.query();
        
      });
})();