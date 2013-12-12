define([
    'jquery',
    'backbone',
    'views/content/content',
    'app'
], function ($, Backbone, ContentView, App) {

    'use strict';

    var Workspace = Backbone.Router.extend({
	
	routes: {
	    'stream/:source/:stream': 'routeStream'
	},
	
	routeStream: function(source, stream){
	    ContentView.routeStream(source, stream);
	}
	
    });

    return Workspace;
    
});
