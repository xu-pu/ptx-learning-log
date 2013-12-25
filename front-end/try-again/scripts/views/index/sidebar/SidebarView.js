define([
    'underscore',
    'marionette',
    'app',
    'text!templates/sidebar.html'
], function (_, Marionette, template) {

    'use strict';

    var SidebarView = Marionette.Layout.extend({
	
//	template: _.template(template),

	regions: {
	    statusBar: '#status-bar',
	    navigationMenu: '#navigation-menu',
	    footerBar: '#footer-bar',
	},

	onRender: function(){
	    this.statusBar.show(new StatusBarView());
	    this.navigationMenu.show(new NavigationMenuView());
	    this.footerBar.show(new FooterBarView());
	},

    });


});
