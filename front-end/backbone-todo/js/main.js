'use strict';

require.config({

    shim: {

	underscore: {
	    exports: '_'
	},

	backbone: {
	    deps: [
		'underscore',
		'jquery'
	    ],
	    exports: 'Backbone'
	},

	backboneLocalstorage: {
	    deps: ['backbone'],
	    exports: 'Store'
	}
    },

    paths: {
	jquery: 'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery',
	underscore: 'http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore-min',
	backbone: 'http://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.0/backbone-min',
	backboneLocalstorage: 'http://cdnjs.cloudflare.com/ajax/libs/backbone-localstorage.js/1.1.0/backbone.localStorage-min',
	text: 'http://cdnjs.cloudflare.com/ajax/libs/require-text/2.0.10/text'
    }

});

require([
    'backbone',
    'views/app',
    'routers/router'
], function (Backbone, AppView, Workspace) {
    
    new Workspace();
    Backbone.history.start();
    new AppView();

});
