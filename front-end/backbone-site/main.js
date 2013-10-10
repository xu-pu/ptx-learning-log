//=========================================================================
// Hello Backbone.js
// this is my hello world program of backbone.js framework 
//=========================================================================
// Model
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

var instance_1 = new DataModel({data1:'data1', data2:'data2'});
var instance_2 = new DataModel();
instance_2.set({data1:'data1', data2:'data2'});

console.log(instance_1.get('data1'));
console.log(instance_2.get('data1'));

instance_1.set({data1: 'new data1'}); // partial change
console.log(instance_1.get('data1'));
console.log(instance_1.get('data2'));


//=========================================================================
// Collection
//=========================================================================

var DataSet = Backbone.Collection.extend({
    model: DataModel
});

var my_dataset = new DataSet([instance_1, instance_2]);

//=========================================================================
// Router (i.e. Controller)
//=========================================================================

var Workspace = Backbone.Router.extend({
    routes: {
	'url1/:param': 'event1',
	'url2/:param': 'event2',
	'url3/:param': 'event3',
    }
});

var app_router = new Workspace;

app_router.on('route:event1', function(param){console.log(param);});
app_router.on('route:event2', function(param){console.log(param);});
app_router.on('route:event3', function(param){console.log(param);});

Backbone.history.start();
