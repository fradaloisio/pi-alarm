/**
*  Module
*
* Description: Main Controller
*/
Client.controller('MainCtrl', ['$scope','$http','getActive','setActive', function ($scope,$http,getActive,setActive) {

	$scope.active =  {checked : false};	

	var statusPromise = getActive.getData();
    statusPromise.then(function(result) {  // this is only run after $http completes
    	if (result == "true") {
      		$scope.active =  {checked : true};
    	}
    	else{
    		$scope.active =  {checked : false};	
    	};
    });	

	$scope.toggleActive = function(){
		console.log('called '+$scope.active.checked);
		setstatusPromise = setActive.setData($scope.active.checked);
		setstatusPromise.then(function(result){
			if (result == "true") {
	      		$scope.active =  {checked : true};
	    	}
	    	else{
	    		$scope.active =  {checked : false};	
	    	};
		});
	};
}]);