//=========================================================================
// Hello Underscore.js
// this is my hello world program of Underscore.js
// tutorial link -- http://net.tutsplus.com/tutorials/javascript-ajax/getting-cozy-with-underscore-js/
//=========================================================================
// List Functionalities
//=========================================================================

// _.select() filter list
var int_list = [3,54,23,45,2,4,435,67,3,35];
var less_list = _.select(int_list, function(num){ return num>50; });
console.log(less_list);
less_list = _(int_list).select(function(num){ return num>50; }); // object-oriented syntax
console.log(less_list);

// _.pluck() dictionary-list to list
var dict_list = [{data1:'data1',data2:'data2'},
		 {data1:'data1',data2:'data2'},
		 {data1:'data1',data2:'data2'}];
var partial_list = _.pluck(dict_list, 'data1');
console.log(partial_list);

// _.map() list comprehension
var symbol_list = _.map(int_list, function(num){
    if (num>50)
	return 1;
    else
	return -1;
});
console.log(symbol_list);

// _.all() traverse and validate the entire list produce one boolean
var is_valid = _.all(int_list, function(num){ return num>50; }); 
console.log(is_valid);

// _.uniq() unique
var repeat_list = [1,1,1,1,1,3,3,2];
var unique_list = _.uniq(repeat_list);
console.log(unique_list);

// _.range()
var range_list = _.range(0,100,10);
console.log(range_list);

// _.intersection()
var conjunction = _.intersection(_.range(0,100,2),
				 _.range(0,100,3),
				 _.range(0,100,4));
console.log(conjunction);


//=========================================================================
// Object Functionalities
//=========================================================================

// _.keys()
var my_dict = {data1:'data1',data2:'data2'};
var dict_keys = _.keys(my_dict);
console.log(dict_keys);

// _.values()
var dict_values = _.values(my_dict);
console.log(dict_values);

// _.defaults()
var my_default = {data1:'data1', data2:'data2', data3:'data3'};
var new_data = _.defaults(my_dict, my_default);
console.log(new_data);


//=========================================================================
// Event functionalities
//=========================================================================

var receiver = {name:'sheep', data1:'data1',data2:'data2'};
var handler = function(param){
    console.log(this.name + ' received message: ' + param);
};
var trigger = _.bind(handler, receiver);
trigger('event happened!')


//=========================================================================
// Template Rendering
//=========================================================================

var content = _.template(jQuery('#my-template').html(), {my_data: 'hello, world'})
jQuery('body').html(content);
