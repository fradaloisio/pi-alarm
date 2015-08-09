Client.factory('setActive', function($http) {

    var setData = function(newStatus) {
        return $http({method:"GET", url:GlobalService.apiUrl+"/api/setStatus?status="+newStatus}).then(function(result){
            return result.data;
        });
    };
    return { setData: setData };
});