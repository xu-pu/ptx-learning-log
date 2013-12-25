define([
    'marionette',
    'application/PageModule',
    'application/AccountModule',
], function(Marionette, PageModule, AccountModule) {

    'use strict';

    var app = new Marionette.Application();

    app.addRegions({
	page: 'body'
    });

    //=======================================
    // display loading page as default
    // initialize AccountModule first
    // initialize ContentModule after account is ready
    //=======================================

    app.module('PageModule', PageModule);
    app.module('ContentModule', ContentModule);
    app.module('AccountModule', AccountModule);

    app.addInitializer(function(){
	this.PageModule.start();
	this.AccountModule.start();
    });

    app.controller = new AppController();

    return app;

});
