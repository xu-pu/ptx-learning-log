var cdn = {
    jquery:     'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min',
    underscore: 'http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore-min',
    backbone:   'http://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.0.0/backbone-min',
    bootstrap:  'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.2/js/bootstrap.min',
    jqueryui:   'http://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min',
    wookmark:   'http://cdnjs.cloudflare.com/ajax/libs/jquery.wookmark/1.3.1/jquery.wookmark.min',
    text:       'http://cdnjs.cloudflare.com/ajax/libs/require-text/2.0.10/text'
};

var local = {
    jquery:     'libs/jquery-2.0.2.min',
    underscore: 'libs/underscore-min',
    backbone:   'libs/backbone-min',
    bootstrap:  '',
    jqueryui:   'libs/jquery-ui',
    wookmark:   'libs/jquery.wookmark.min',
    text:       ''
};

require.config({

    paths: local,

    shim: {

	'marionettee': {
	    deps: ['backbone'],
	    exports: 'Backbone.Marionette'
	},

	'backbone': {
	    deps: [
		'underscore', 
		'jquery'
	    ],
	    exports: 'Backbone'
	},

	'underscore': {
	    exports: '_'
	},

	'jquery': {
	    exports: 'jQuery'
	},

	'jqueryui': {
	    deps: [
		'jquery'
	    ],
	    exports: '$'
	},

	'wookmark': {
	    deps: [
		'jquery',
		'jqueryui'
	    ],
	    exports: '$'
	}
    },

    deps: ['jquery', 'underscore']

});


require([
    'app',
    'backbone',
    'routers/index',
    'controllers/index'
], function (app, Backbone, Router, Controller) {
    
    'use strict';

    app.start();

    new Router({ controller: Controller });

    Backbone.history.start();

}); 
