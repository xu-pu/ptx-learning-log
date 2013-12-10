define([
    'jquery',
    'backbone'
], function ($, Backbone) {

    var FeedView = Backbone.View.extend({

	tagName: 'div',
	className: 'grid-item',

	initialize: function(){
	    this.render();
	},

	render: function(){
	    this.$el.html('Hello');
	    if (this.model.get('type') === 1) {
		this.$el.addClass('type1');
	    }
	    else {
		this.$el.addClass('type2');
	    }
	    return this.$el;
	}

    });

    return FeedView;

});
