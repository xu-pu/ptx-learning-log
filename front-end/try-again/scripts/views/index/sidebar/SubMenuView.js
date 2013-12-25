define([

], function () {

    'use strict';

    var SubMenuView = Marionette.Layout.extend({
	
	regions: {
	    tab: '.menu',
	    entries: '.submenu',
	},

	initialize: function(){
	    this.category = this.model;
	    this.streams = this.model.streams;
	},

	onRender: function(){
	    this.tab.show(new MenuTabView({
		model: this.category,
	    }));
	    this.entries.show(new EntriesView({
		collection: this.streams,
	    }));
	},

    });

    return SubMenuView;

});
