define([
    'jquery',
    'backbone',
    'jqueryui',
    'wookmark'
], function ($, Backbone) {

    var ContainerView = Backbone.View.extend({
	
	el: '#main',

	initialize: function(){
	    
	    this.$grid = $('#grid-container');
	    
	    this.$('.grid-item').wookmark({
		container: this.$grid,
		align: 'left',
		offset: 8
	    });

	},

	render: function(){

	}

    });

    return new ContainerView();

});
