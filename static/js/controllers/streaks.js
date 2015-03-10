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
        $scope.streak = Streak.query();
      });
})();