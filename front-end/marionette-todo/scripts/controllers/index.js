define([
    'app'
], function (app) {

    'use strict';

    var Controller = {
	setFilter: function(param){
	    app.vent.trigger('todoList:filter', param && param.trim() || '');
	}
    };

    return Controller;

});
