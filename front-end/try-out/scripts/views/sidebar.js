define([
    'jquery',
    'underscore',
    'backbone',
    'views/tab'
], function ($, _, Backbone, TabView) {

    var SidebarView = Backbone.View.extend({

	el: '#sidebar',

	initialize: function(){
	    this._tabs = _.map(this.$('.item', this.$el), function(e){ return new TabView({ el: e }); });
	}
	
    });
    
    return new SidebarView();

});
