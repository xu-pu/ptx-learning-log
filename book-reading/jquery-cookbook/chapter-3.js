//==========================================================================
// <jQuery Cookbook> Chapter #3 -- Beyond basics
//==========================================================================

(function($){
    $(document).ready(function(){
	
	// iterate inside a collection
	$('div').each(function(){
	    $(this).addClass('someClass');
	});

	// select perticular item inside collection
	$('div')
	    .eq(0) // index start from 0
	    .css('attr','value');

	// get raw DOM instead of jQuery object
	var raw_div = $('div')[0];
	var raw_div_array = $('div').get();

	// get index of object within a collection
	$('div').click(function(){
	    var index = $('div').index(this);
	});
	
	// map (list comprehension)
	var new_array = $.map($('li'), function(item, index) {
	    if (index < 3) 
		return $(item).html;
	    else 
		return null;
	});

	// operate on a subset
	$('div')
	    .slice(n) // [n,end]
	    .end()
	    .slice(m, n); // [m,n)

	// avoid conflict with other libs
	jQuery.noConflict(); // unlink symbol $
	var j = jQuery.noConflict(); // assign to name j
	// use closure to encapsulate jQuery
	jQuery.noConflict(); 
	(function($){
	    // code
	})(jQuery);


	// add jQuery plugins
	$('selector').thePlugin(param);
	$.fn.myPlugin = function(){};

	// introspection
	$('div').selector; // 'div'
	$('div').context; // HTMLDocument

    });
})(jQuery);
