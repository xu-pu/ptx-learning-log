define([

], function () {

    'use strict';

    var MenuTabView = Marionette.ItemView.extend({
	
	ui: {
	    title: '.tiitle',
	    indicator: '.indicator',
	},

    });

    return MenuTabView;
    
});
