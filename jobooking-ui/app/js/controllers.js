var jobookingControllers = angular.module('jobookingControllers', ['ui.bootstrap']);
jobookingControllers.controller('CatagoryListCtrl', function ($scope, $http) {
    
	$http.get('phones/catagories.json').success(function(data) {
	    $scope.catagories = data;
	  });
});


jobookingControllers.controller('LoginCtrl', function ($scope, $http) {
    
	$http.get('phones/catagories.json').success(function(data) {
	    $scope.catagories = data;
	  });
});