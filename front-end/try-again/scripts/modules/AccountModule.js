define([], function () {

    'use strict';

    var AccountModule = function(module, app) {
	module.startWithParent = false;
	module.on('start', function(){
	    module.controller = new AccountController();
	});
    };

    return AccountModule;

});
