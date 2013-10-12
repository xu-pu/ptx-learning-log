//=========================================================================
// Hello Backbone.js
//=========================================================================

// this is my hello world program of backbone.js framework 
// objective -- implement a fake-AJAX infinite feed stream

//=========================================================================
// Model and Model Collection
//=========================================================================

var DataModel = Backbone.Model.extend({
    initialize: function(){
	this.on('change:data1', function(model){
	    console.log('data1 changed to ' + model.get('data1'));
	});
    },

    defaults: {
	data1: 'data1',
	data2: 'data2'
    }
});


var DataSet = Backbone.Collection.extend({
    model: DataModel
});

//=========================================================================
// View
//=========================================================================

var ModuleView = Backbone.View.extend({
    initialize: function(){
	this.render();
    },
    render: function(){
	console.log(this.model.attributes);
	var str_dom = _.template(jQuery('#module-template').html(), this.model.attributes);
	this.el = jQuery(str_dom);
	return this;
    } 
});

var CollectionView = Backbone.View.extend({
    initialize: function(){
	this.render_head = 0;
	this.module_views = [];
	this.listenTo(this.collection, 'add', this.render);
    },
    render: function(){
	var self = this;
	this.collection.rest(this.render_head).forEach(function(new_model){
	    var new_view = new ModuleView({model: new_model});
	    self.module_views.push(new_view);
	    self.$el.append(new_view.el);
	});
	this.render_head = this.collection.length;
    }
});

//=========================================================================
// Business Model
//=========================================================================

var stream_model = new DataSet();

var stream_view = new CollectionView({
    collection: stream_model,
    el: jQuery('#content-container')
});

stream_model.add(new DataModel);
stream_model.add(new DataModel);

//=========================================================================
// Router (i.e. Controller)
//=========================================================================

var Workspace = Backbone.Router.extend({
    routes: {
	'url1/:param': 'event1',
	'url2/:param': 'event2',
	'url3/:param': 'event3',
    },

    event1: function(param){ console.log(param); },

    event2: function(param){ console.log(param); }
});

var app_router = new Workspace;

app_router.on('route:event3', function(param){console.log(param);});

Backbone.history.start();
