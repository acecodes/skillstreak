(function() { 
    'use strict';

    /**
     * @ngdoc function
     * @name frontendApp.controller:AboutCtrl
     * @description
     * # AboutCtrl
     * Controller of the frontendApp
     */
    angular.module('streakApp')
      .controller('StreakCtrl', function ($scope, djResource) {
        var Streak = djResource('/api/streaks/:streakId', {streakId:'@id'});
        $scope.streak = Streak.query();
      });
})();