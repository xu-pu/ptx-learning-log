define([
    'jquery',
    'backbone',
    'views/content/feed',
    'jqueryui',
    'wookmark'
], function ($, Backbone, FeedView) {

    var StreamView = Backbone.View.extend({
	
	el: '#stream',
	
	events: {
	    'click #stream-more': 'loadMore'
	},

	initialize: function(){
	    this.$body = $('#stream-body');
	    this.$load = $('#stream-more');

	    this.listenTo(this.collection, 'add', this.addOne);

	    this._feeds = [];	    
	    this.collection.fetch();
	},

	loadMore: function(){
	    this.collection.fetch();
	},

	addOne: function(feed){
	    var new_feed = new FeedView({ model: feed });
	    this._feeds.push(new_feed);
	    this.$body.append(new_feed.$el);

	    this.$('.grid-item').wookmark({
	    	container: this.$body,
	    	align: 'left',
	    	offset: 8
	    });	    
	}

    });

    return StreamView;

});
