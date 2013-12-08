require.config({

    shim: {

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
	}

    },

    paths: {
	jquery:     'http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min',
	underscore: 'http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore-min',
	backbone:   'http://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.0.0/backbone-min',
	bootstrap:  'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.2/js/bootstrap.min',
	jqueryui:   'http://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min',
	text:       'http://cdnjs.cloudflare.com/ajax/libs/require-text/2.0.10/text'
    }

});

require([
    'views/sidebar'
], function (SidebarView) {
    
    var sidebar = SidebarView;

}); 
