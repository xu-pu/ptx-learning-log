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

    app.module('Account', AccountModule);
    app.module('Page', PageModule);
    app.module('Index', IndexModule);
    app.module('Content', ContentModule);

    app.addInitializer(function(){
    });

    return app;

});
