define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {

    'use strict';

    var FeedModel = Backbone.Model.extend({

	idAttribute: 'cid',
	
	defaults: { 
	    type: 1,
	    read: false
	}

    });

    return FeedModel;

});
