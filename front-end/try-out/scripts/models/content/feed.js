define([
    'jquery',
    'backbone'
], function ($, Backbone) {

    var FeedModel = Backbone.Model.extend({
	
	defaults: { type: 1 }

    });

    return FeedModel;

});
