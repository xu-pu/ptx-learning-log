define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {

    'use strict';

    var FeedView = Backbone.View.extend({

	// model : FeedModel

	tagName: 'div',

	className: 'grid-item',

	initialize: function(){
	    this.render();
	},

	render: function(){
	    this.$el.html(_.result(this.model, 'url'));
	    if (this.model.get('type') === 1) {
		this.$el.addClass('type1');
	    }
	    else {
		this.$el.addClass('type2');
	    }
	    return this;
	}

    });

    return FeedView;

});
