Client.factory('getActive', function($http) {

    var getData = function() {
        return $http({method:"GET", url:GlobalService.apiUrl+"/api/getStatus"}).then(function(result){
            return result.data;
        });
    };
    return { getData: getData };
});