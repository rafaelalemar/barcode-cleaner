//angular.module('app', []);

//$(function(){
    angular.module('app', [])
        .config(function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
        })

        .controller('codBarrasController', ['$scope', function($scope) {
           $scope.clearBarcode = function(){
               if ($scope.barcode)
                return $scope.barcode.replace(/\D+/g, "");
               return "";
           }
        }])
//});


