define([
    'jquery',
    'underscore',
    'backbone'
], function ($, _, Backbone) {

    var EntryView = Backbone.View.extend({
	
	tagName: 'li',

	className: 'subitem',

	initialize: function(){
	    this.render_first();
	    this.listenTo(this.model, 'change:residue', this.render_indicator);
	},

	render_first: function(){
	    this.$body = $('<a>').html(this.model.get('name')).appendTo(this.$el);
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
