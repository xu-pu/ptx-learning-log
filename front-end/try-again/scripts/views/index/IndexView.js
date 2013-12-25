define([

], function () {

    'use strict';

    var IndexView = Marionette.Layout.extend({

	regions: {
	    sidebar: '#sidebar',
	    content: '#content',
	},

	onRender: function(){
	    this.sidebar.show(new SidebarView());
	    this.content.show(new ContentView());
	},

    });

    return IndexView;

});
