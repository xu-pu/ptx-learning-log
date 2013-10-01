//==========================================================================
// <jQuery Cookbook> Chapter #4 -- jQuery Utilities
//==========================================================================

(function($){
    
    // detect presence of jQury functionality
    if ($.support.herfNormalized)
	alert('suppoerted')

    // iterate with $.each()
    var my_list = [1,2,3,4,5,6];
    $.each(my_list, function(index, value){
	// this === current element
    });

    // filter array with $.grep()
    var my_list = [1,2,3,4,5,6];
    $.grep(my_list, function(value,index){
	// return true if accept
	// filter is for jQuery objects, grep for list
    });

    // list comprehension
    var my_list = [1,2,3,4,5,6];
    var result = $.map(my_list, function(value, index){
	// return new value
    });

    // merge array
    var list_1 = [1,2,3,4,5];
    var list_2 = [6,7,8,9];
    var list_new = $.merge(list_1, list_2);

    // eliminate duplicates
    var my_list = [1,2,2,3,3,3,4];
    var new_list = $.unique(my_list)

    // test is object a function
    if ($.isFunction(element.onClick))
	elememt.onClick.call(this);

    // remove white spaces from string
    $('p').each(function(){
	var tmp = $.trim($(this).val());
	$(this).val(tmp);
    });

    // add metadata to DOM objects without memory leak
    $('#selector').data('name', {key:'value'});
    var get_metadata = $('#selector').data('name');

    // extend object
    var default_options = {a:'valuea', b:'valueb'};
    // the later one overrides the former one
    var opetions = $.extend(default_options, your_opetion); 
    // if the first is true, deep copy
    var obj1 = {a:{a:'valuea', b:'valueb'}};
    var obj2 = {a:{a:'valuea', c:'valuec'}};
    var obj3 = $.extend(true, obj1, obj2);

})(jQuery);
