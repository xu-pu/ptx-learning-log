define([
    'modules/page/PageController',
], function (PageController) {

    'use strict';

    var PageModule = function (module, parent) {
	
	var app = parent;

	module.startWithParent = false;
	module.region = app.page;

	module.on('start', function(options){

	});

	module.addInitializer(function(options) {
	    module.state = 'loading';
	    module.region.show(new LoadingScreen());
	    module.listenTo(app.vent, 'account:ready', this.onAccountReady);
	    module.listenTo(app.vent, 'account:fail', this.onAccountFail);
	    module.listenTo(app.vent, 'index:ready', this.onIndexReady);  
	});

	onAccountReady: function(){
	    if (module.state === 'loading') {
		module.region.currentView.triggerMethod('account:ready');
	    };	    
	},

	onAccountFail: function(){
	    module.region.show(new WelcomeScreen());
	},

	onContentReady: function(){
	    module.region.show(new IndexView());
	},

    };

    return PageModule;

});
