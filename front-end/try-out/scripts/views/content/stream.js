define([
    'jquery',
    'underscore',
    'backbone',
    'views/content/feed',
    'jqueryui',
    'wookmark'
], function ($, _, Backbone, FeedView) {

    'use strict';

    var StreamView = Backbone.View.extend({
	
	// model: StreamModel

	tagName: 'div',

	className: 'stream',
	
	events: {
	    'click .stream-more': 'loadMore'
	},

	initialize: function(){
	    this.createDOM();
	    this._feeds = [];

	    this.listenTo(this.model.feeds, 'add', this.addOne);
	    this.listenTo(this, 'mount', this.onMount);
	    this.listenTo(this, 'organize', this.organize);
	    this.listenTo(this.model, 'change:residue', this.organize);
	    
	    if (this.model.ready){
		this.render();
	    }
	    else{
		this.model.getReady();
	    }
	},

	onMount: function(){
	    this.organize();
	    this.delegateEvents();
	},

	createDOM: function(){
	    this.$body = $('<div>').addClass('stream-body');
	    this.$load = $('<div>')
		.addClass('stream-more')
		.html(_.result(this.model, 'url'));
	    this.$el.append(this.$body);
	    this.$el.append(this.$load);
	},

	render: function(){
	    this.model.feeds.each(this.addOne, this);
	},

	loadMore: function(){
	    this.model.fetch();
	},

	addOne: function(feed){
	    var new_feed = new FeedView({ model: feed });
	    this._feeds.push(new_feed);
	    new_feed.$el.hide();
	    this.$body.append(new_feed.$el);
	    new_feed.$el.fadeIn('slow');
	    this.organize();
	},

	organize: function(){
	    this.$('.grid-item').wookmark({
	    	container: this.$body,
	    	align: 'left',
	    	offset: 8
	    });
	    console.log('re-organized');
	}

    });

    return StreamView;

});
