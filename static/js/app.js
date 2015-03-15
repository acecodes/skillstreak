(function() {
    'use strict';

    /**
     * @ngdoc overview
     * @name streakApp
     * @description
     * # streakAppp
     *
     * Main module of the application.
     */
    angular.module('streakApp', [
        'djangoRESTResources',
        'ngCookies',
        'ngResource',
        'ui.router'
    ]).
    config(['$httpProvider',
        function($httpProvider, $cookies) {
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        }
    ]).
    config(function ($stateProvider) {
        var views = "/static/js/views/";
        $stateProvider.state("dashboard", {
            url: "",
            controller: "StreakController as streakCtrl",
            templateUrl: views + "streaks.html"
        });
    });
})();