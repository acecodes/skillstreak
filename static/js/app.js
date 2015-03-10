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
    angular.module('streakApp', ['djangoRESTResources', 'ngCookies', 'ngResource', 'ngRoute']).
  config(['$httpProvider', function($httpProvider, $cookies){
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  }]);
})();