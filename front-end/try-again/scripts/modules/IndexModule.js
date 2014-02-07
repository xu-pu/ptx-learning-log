define([

], function () {
    
    'use strict';

    var IndexModule = function(self, app){

	self.addInitializer(function(){

	});

	self.on('start', function(){});

	self.listenTo(app.vent, 'content:ready', function(){
	    self.view = new IndexView({ collection: app.module('Account').categories })
	});

    };

    return IndexModule;

});
