define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {

    'use strict';

    var EntryView = Backbone.View.extend({

	// model: StreamModel

	tagName: 'li',

	className: 'subitem',

	initialize: function(){
	    this.href = '#/stream/' + this.model.collection.source.get('name') + '/' + this.model.get('name');
	    this.createDOM();
	    this.listenTo(this.model, 'change:residue', this.render_indicator);
	},

	createDOM: function(){
	    this.$body = $('<a>')
		.html(this.model.get('name'))
		.attr({ 'href': this.href })
		.appendTo(this.$el);
	    this.$indicator = $('<span>')
		.addClass('indicator')
		.html(this.model.get('residue'))
		.appendTo(this.$body);
	    return this;
	},

	render_indicator: function(){
	    this.$indicator.html(this.model.get('residue'));
	    return this;
	}
	
    });
    
    return EntryView;
    
});
