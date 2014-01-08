define([
    'jquery',
    'underscore',
    'backbone',
    'models/sources',
    'views/content/stream',
], function ($, _, Backbone, SourcesModel, StreamView) {

    'use strict';

    var ContentView = Backbone.View.extend({
	
	el: '#main',

	routeStream: function(source, stream){
	    this.currentStream = SourcesModel.get(source).streams.get(stream);
	    this._currentStream = new StreamView({ model: this.currentStream });

	    if (this.$stream == null) {
		this.$stream = this._currentStream.$el.appendTo(this.$el);
	    }
	    else {
		this.$el.html('');
		this.$stream = this._currentStream.$el.appendTo(this.$el);
	    }
	    this._currentStream.trigger('mount');
	}
	
    });
    
    return new ContentView();

});
