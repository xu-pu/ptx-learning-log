define([
    'jquery',
    'underscore',
    'backbone',
    'views/sidebar/submenu',
    'models/sidebar/menu'
], function ($, _, Backbone, SubMenuView, MenuModel) {

    var SidebarView = Backbone.View.extend({

	el: '#sidebar',
	
	className: 'sidebar',

	initialize: function(){
	    this.render_first();
	    this._submenus = [];
	    this.listenTo(this.model, 'add', this.addSubMenu)
	    this.model.fetch();
	},
	
	render_first: function(){
	    this.$menu = $('<ul>').addClass('menu').appendTo(this.$el);
	    return this;
	},

	addSubMenu: function(sub){
	    var new_sub = new SubMenuView({ model: sub });
	    this._submenus.push(new_sub);
	    this.$menu.append(new_sub.$el);
	}

    });

    return new SidebarView({ model: MenuModel });

});
