define([
    'jquery',
    'underscore',
    'backbone',
    'models/sidebar/entry'
], function ($, _, Backbone, EntryModel) {

    var SubMenuModel = Backbone.Model.extend({
	
	initialize: function(){
	    this.entries = new Backbone.Collection([], { model: EntryModel });
	    this.listenTo(this.entries, 'add', this.addEntry);
	},

	addEntry: function(model){
	    this.trigger('add', model);
	},

	fetch: function(){
	    var self = this;
	    var entries = ['Friends','Videos','Galleries','Podcasts','Robots'];
	    _.each(entries, function(entry){
		self.entries.push(new EntryModel({ name: entry, residue: 100 }));
	    });
	},

	getResidue: function(){
	    return this.entries.reduce(function(sum, entry){ return sum + entry.get('residue'); }, 0);
	}

    });

    return SubMenuModel;

});
