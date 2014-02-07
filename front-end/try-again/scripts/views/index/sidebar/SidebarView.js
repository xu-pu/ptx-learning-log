define([
    'underscore',
    'marionette',
    'app',
    'text!templates/sidebar.html'
], function (_, Marionette, app, template) {

    'use strict';

    var SidebarView = Marionette.Layout.extend({
	
	template: _.template(template),

	regions: {
	    statusBar: '#status-bar',
	    navMenu: '#nav-menu',
	    footerBar: '#footer-bar',
	},

	initialize: function(){
	    this.categories = this.collection;
	},

	onRender: function(){
	    this.statusBar.show(new StatusBarView());
	    this.navMenu.show(new NavMenuView({ collection: this.categories }));
	    this.footerBar.show(new FooterBarView());
	},

    });

    return SidebarView;

});
