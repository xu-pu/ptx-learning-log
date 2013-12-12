define([
    'jquery',
    'underscore',
    'backbone',
    'models/stream',
], function ($, _, Backbone, StreamModel) {

    'use strict';

    var SourceModel = Backbone.Model.extend({

	defaults: { 
	    name: 'root',
	    residue: 0
	},
	
	idAttribute: 'name',

	initialize: function(){
	    var StreamsCollection = Backbone.Collection.extend({
		source: this,
		model: StreamModel,
		url: _.result(this, 'url') + '/streams'
	    });
	    this.streams = new StreamsCollection();
	    this.listenTo(this.streams, 'change:residue', this.syncResidue)
	    this.listenTo(this.streams, 'add', this.addStream);
	},

	addStream: function(stream){
	    this.trigger('add', stream);
	},

	fetch: function(){
	    var self = this;
	    var streams = ['Friends','Videos','Galleries','Podcasts','Robots'];
	    _.each(streams, function(stream){
		var new_stream = new StreamModel({ name: stream }, 
						 { collection: self.streams });
		self.streams.push(new_stream);
	    });
	},

	syncResidue: function(){
	    var r = this.streams.reduce(function(sum, stream){ return sum + stream.get('residue'); }, 0);
	    this.set('residue', r);
	}

    });

    return SourceModel;

});
