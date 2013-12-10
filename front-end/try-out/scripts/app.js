define([
    'models/content/stream',
    'views/sidebar/sidebar',
    'views/content/stream',
], function (StreamModel, SidebarView, StreamView) {

    var App = {

	models: {},

	views: {
	    sidebar: SidebarView,
	},

	initialize: function(){
	    this.models.stream = new StreamModel();
	    this.views.stream = new StreamView({ collection: this.models.stream });
	}

    };

    return App;

});
