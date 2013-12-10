define([
    'jquery',
    'underscore',
    'backbone',    
], function ($, _, Backbone) {

    var EntryModel = Backbone.Model.extend({
	
	defaults: {
	    name: 'default name',
	    residue: 0
	}

    });

    return EntryModel;

});
