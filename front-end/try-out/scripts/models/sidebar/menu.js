define([
    'jquery',
    'underscore',
    'backbone',
    'models/sidebar/submenu'
], function ($, _, Backbone, SubMenuModel) {

    var MenuModel = Backbone.Model.extend({

	initialize: function(){
	    this.submenus = new Backbone.Collection([], { model: SubMenuModel });
	    this.listenTo(this.submenus, 'add', this.addSubMenu);
	},

	addSubMenu: function(model){
	    this.trigger('add', model);
	},

	fetch: function(){
	    var self = this;
	    var submenus = ['Friends','Videos','Galleries','Podcasts','Robots'];
	    _.each(submenus, function(submenu){
		self.submenus.push(new SubMenuModel({ name: submenu }));
	    });
	}

    });

    return new MenuModel();

});
