'use strict';

/**
 * @ngdoc overview
 * @name myApp
 * @description
 * # myApp
 *
 * Main module of the application.
 */
angular
  .module('myApp', [
    'ngAnimate',
    // 'ngCookies',
    //'ngResource',
    'ngRoute'
    //'ngSanitize'
  ])
  .constant('config', {
    staticUrl: window.staticUrl,
    csrfToken: window.csrfToken
  })
  .config(function ($routeProvider, $locationProvider, $httpProvider) {
    // Pass csrfToken with each ajax request
    $httpProvider.defaults.headers.common['X-CSRFToken'] = window.csrfToken;

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'ctrl'
      })
      .otherwise({
        redirectTo: '/'
      });

    $locationProvider.html5Mode({enabled: true, requireBase: false});
  })
  .run(function () {
    FastClick.attach(document.body);
  });
