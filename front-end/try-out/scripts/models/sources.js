define([
    'jquery',
    'underscore',
    'backbone',
    'models/source',
    'app'
], function ($, _, Backbone, SourceModel, App) {

    'use strict';

    var SourcesModel = Backbone.Collection.extend({

	url: '/sources',

	model: SourceModel,

	fetch: function(){
	    var self = this;
	    var sources = ['Friends','Videos','Galleries','Podcasts','Robots'];
	    _.each(sources, function(source){
		self.push(new SourceModel({ name: source }, { collection: self }));
	    });
	}

    });

    return new SourcesModel();

});
