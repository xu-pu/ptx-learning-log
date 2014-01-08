define([

], function () {

    'use strict';

    var PageModule = function (self, app) {
	
	self.region = app.page;

	self.on('start', function(options){

	});

	self.addInitializer(function(options) {
	    self.state = 'loading';
	    self.region.show(new LoadingScreen());
	    self.listenTo(app.vent, 'account:ready', self.onAccountReady);
	    self.listenTo(app.vent, 'account:fail', self.onAccountFail);
	    self.listenTo(app.vent, 'index:ready', self.onIndexReady); 
	});

	self.onAccountReady = function(){
	    if (self.state === 'loading') {
		self.region.currentView.triggerMethod('account:ready');
	    };
	};

	self.onAccountFail = function(){
	    self.state = 'welcome';
	    self.region.show(new WelcomeScreen());
	};

	self.onIndexReady = function(){
	    self.state = 'index';
	    self.region.show(app.IndexModule.view);
	};

    };

    return PageModule;

});
