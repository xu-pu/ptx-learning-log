define([

], function () {

    'use strict';

    var IndexView = Marionette.Layout.extend({

	regions: {
	    sidebar: '#sidebar',
	    content: '#content',
	},

	initialize: function(options){
	    this.categories = this.collection;
	},

	onRender: function(){
	    this.sidebar.show(new SidebarView({ collection: this.categories }));
	    this.content.show(new EmptyContentView());
	},

	onRenderStream: function(stream){
	    this.content.show(new StreamView({ model: stream }));
	},

    });

    return IndexView;

});
