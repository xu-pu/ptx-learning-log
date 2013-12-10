define([
    'jquery',
    'underscore',
    'backbone',
    'views/sidebar/entry'
], function($, _, Backbone, EntryView) {

    var SubMenuView = Backbone.View.extend({

	tagName: 'li',
	className: 'item',

        events: {
            'click .sidebar-tab': 'toggleTab',
        },

        initialize: function() {
	    this.render_first();
            this.active = false;
	    this._entries = [];

	    this.listenTo(this.model, 'add', this.addEntry);
	    
	    this.model.fetch();
        },

	addEntry: function(entry){
	    var new_entry = new EntryView({ model: entry });
	    this.$body.append(new_entry.$el);
	    this._entries.push(new_entry);
	    this.render_indicator();
	},

	render_first: function(){
	    this.$tab = $('<a>').addClass('sidebar-tab').html(this.model.get('name')).appendTo(this.$el);
	    this.$body = $('<ul>').addClass('sidebar-tab-body').appendTo(this.$el);
	    this.$indicator = $('<span>')
		.addClass('indicator')
		.html(this.model.getResidue())
		.appendTo(this.$tab);
	    this.$body.hide();
	},

	render_indicator: function(){
	    this.$indicator.html(this.model.getResidue());
	},

        toggleTab: function() {
            if (this.active) {
                this.active = false;
                this.$body.stop(true, true).slideUp('normal')
            } else {
                this.active = true;
                this.$body.filter(':visible').slideUp('normal');
                this.$body.stop(true, true).slideDown('normal');
            }
        }

    });

    return SubMenuView;

});
