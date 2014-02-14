define([], function () {

    'use strict';

    var AccountModule = function(module, app) {

	module.on('start', function(){
	    module.controller = new AccountController();
	});

    };

    return AccountModule;

});
