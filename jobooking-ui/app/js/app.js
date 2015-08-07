var jobookingApp = angular.module('jobookingApp', [
                                                 'ngRoute',
                                                 'jobookingControllers'
                                               ]);


jobookingApp.config(['$routeProvider',
                    function($routeProvider) {
                      $routeProvider.
                        when('/', {
                          templateUrl: 'partials/login-modal.html',
                          controller: 'LoginCtrl'
                        }).
                        otherwise({
                          redirectTo: '/'
                        });
                    }]);