define([
    'jquery',
    'underscore',
    'backbone',
    'models/feed',
], function ($, _, Backbone, FeedModel) {

    'use strict';

    var StreamModel = Backbone.Model.extend({

	defaults: {
	    name: 'root',
	    residue: 0
	},

	idAttribute: 'name',

	initialize: function(){
	    var FeedsCollection = Backbone.Collection.extend({
		model: FeedModel, 
		url: _.result(this, 'url') 
	    });
	    this.feeds = new FeedsCollection();
	    this.listenTo(this.feeds, 'all', this.passEvent);
	    this.listenTo(this.feeds, 'add', this.addFeed);
	    this.listenTo(this.feeds, 'change:read', this.toggleRead)
	},

	toggleRead: function(feed){
	    if (feed.get('read')) {
		this.set('residue', this.get('residue')-1)
	    }
	    else {
		this.set('residue', this.get('residue')+1)
	    }
	},

	addFeed: function(){
	    this.set('residue', this.get('residue')+1);
	},

	getReady: function(){
	    if (!this.ready) {
		this.ready = true;
		this.fetch();
	    }
	},

	passEvent: function(){
	    this.trigger.apply(this, arguments);
	},

	fetch: function(){
	    var self = this;
	    var sample = [1,2,2,1,1,2,1,2];
	    _.each(sample, function(n){
		self.feeds.push(new FeedModel({ type: n }, { collection: self.feeds }));
	    });
	}

    });

    return StreamModel;

});
