define([
    'jquery',
    'underscore',
    'backbone',
    'views/sidebar/submenu',
    'models/sources'
], function ($, _, Backbone, SubMenuView, SourcesModel) {

    'use strict';

    var SidebarView = Backbone.View.extend({

	el: '#sidebar',
	
	className: 'sidebar',

	initialize: function(){
	    this.createDOM();
	    this._submenus = [];
	    this.listenTo(this.model, 'add', this.addSubMenu)
	    this.model.fetch();
	},
	
	createDOM: function(){
	    this.$menu = $('<ul>').addClass('menu').appendTo(this.$el);
	    return this;
	},

	addSubMenu: function(source){
	    var new_sub = new SubMenuView({ model: source });
	    this._submenus.push(new_sub);
	    this.$menu.append(new_sub.$el);
	}

    });

    return new SidebarView({ model: SourcesModel });

});
