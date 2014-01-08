define([
    'backbone',
    'models/sources',
    'views/sidebar/sidebar',
    'views/content/stream',
    'views/content/content',
    'router'
], function (Backbone, SourcesModel, SidebarView, StreamView, ContentView, Workspace) {

    'use strict';

    var App = {

	models: {
	    sources: SourcesModel
	},

	views: {
	    sidebar: SidebarView,
	    content: ContentView
	},

	initialize: function(){
	    this.router = new Workspace();
	    Backbone.history.start();
	}

    };

    return App;

});
