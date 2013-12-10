define([
    'jquery',
    'backbone',
    'models/content/feed',
], function ($, Backbone, FeedModel) {

    var StreamModel = Backbone.Collection.extend({

	model: FeedModel,

	fetch: function(){
	    var self = this;
	    var sample = [1,2,2,1,1,2,1,2];
	    _.each(sample, function(n){
		self.push(new FeedModel({ type: n }));
	    });
	}

    });

    return StreamModel;

});
