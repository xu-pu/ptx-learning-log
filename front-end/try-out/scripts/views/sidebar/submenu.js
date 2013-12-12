define([
    'jquery',
    'underscore',
    'backbone',
    'views/sidebar/entry'
], function($, _, Backbone, EntryView) {

    var SubMenuView = Backbone.View.extend({

	// model: SourceModel

	tagName: 'li',

	className: 'item',

        events: {
            'click .sidebar-tab': 'toggleTab',
        },

        initialize: function() {
	    this.createDOM();
            this.active = false;
	    this._entries = [];
	    this.listenTo(this.model, 'add', this.addEntry);
	    this.listenTo(this.model, 'change:residue', this.render_indicator);
	    this.model.fetch();
        },


	createDOM: function(){
	    this.$tab = $('<a>').addClass('sidebar-tab').html(this.model.get('name')).appendTo(this.$el);
	    this.$body = $('<ul>').addClass('sidebar-tab-body').appendTo(this.$el);
	    this.$indicator = $('<span>')
		.addClass('indicator')
		.html(this.model.get('residue'))
		.appendTo(this.$tab);
	    this.$body.hide();
	},

	addEntry: function(stream){
	    var new_entry = new EntryView({ model: stream });
	    this.$body.append(new_entry.$el);
	    this._entries.push(new_entry);
	    this.render_indicator();
	},

	render_indicator: function(){
	    this.$indicator.html(this.model.get('residue'));
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
