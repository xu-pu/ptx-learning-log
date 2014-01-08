define([
    'backbone',
    'models/Feed',
], function (Backbone, Feed) {

    'use strict';

    var Feeds = Backbone.Collection.extend({
	model: Feed
    });

    return Feeds;

});
