define([

], function () {

    'use strict';

    var EntryView = Marionette.ItemView.extend({

	ui: {
	    title: '.tiitle',
	    indicator: '.indicator',
	},

    });
    
    return EntryView;

});
