define([

], function () {

    'use strict';

    var ContentModule = function(self, app){

	self.on('start', function(){
	    self.categories = new Categories();
	    self.streams = new Streams();
	});

	self.listenTo(app.vent, 'account:ready', function(){
	    self.categories.fetch();
	    self.streams.fetch();
	    app.vent.trigger('content:ready');
	});
    };

    return ContentModule;

});
