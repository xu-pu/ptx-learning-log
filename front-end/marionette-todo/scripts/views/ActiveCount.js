define([
    'marionette',
    'jquery'
], function (Marionette, $) {

    'use strict';

    var ActiveCountView = Marionette.View.extend({

	initialize: function(){
	    this.listenTo(this.collection, 'all', this.render, this);
	},

	render: function(){
	    this.$el = $('#todo-count');

	    var itemLeft = this.collection.getActive().length;
	    var itemWord = itemLeft < 1 || itemLeft > 1 ? 'items' : 'item';

	    this.$el.html('<strong>' + itemLeft + '</strong>' + itemWord + ' left');
	}

    });

    return ActiveCountView;

});
