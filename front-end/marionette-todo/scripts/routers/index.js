define([
    'marionette'
], function (Marionette) {

    'use strict';

    var Workspace = Marionette.AppRouter.extend({
	appRoutes: {
	    '*filter': 'setFilter'
	}
    });

    return Workspace;

});
