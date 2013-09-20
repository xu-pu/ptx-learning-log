/*
 * Reading <jQuery Cookbook> chapter #1
 * following are some sample code
 */

(function($){

    $(document).ready(function(){ // ready event triggers when DOM is loaded

	$('div').hide(); // hide element
	$('div').text('new text'); // update text
	$('div').addClass('newclass'); // add class to element
	$('div').show(); // un-hide element

	// chaining operation
	$('div')
	    .hide()
	    .text('new text')
	    .addClass('newclass')
	    .show();

	var txt = $('p').text(); // text() with no args return current text 

	var num = $('a').length; // amount of selected element

	// select element under certain context
	$('input', $('form'));
	$('input', 'body');

	// filtering element
	$('div')
	    .filter(function(index){
		return $(this).hasClass('external'); })
	    .length;
	
	// search including children
	$('div')
	    .find('a')
	    .length;
	
	// destructive change and fallback
	$('div')
	    .find('a')
	    .filter('.someClass')
	    .end()
	    .end();

	// combine search result and domain
	$('div')
	    .find('p')
	    .andSelf()
	    .css('border','1px solid');

	// traverse
	var list = $('li:eq(0)')
	for (var i=0; i<5; i++) {
	    list.css('border').next();
	}

	// select within current context
	$('li:eq(1)')
	    .next()
	    .prev()
	    .parent()
	    .children(':last')

	$('li:eq(1)').prevAll();
	$('li:eq(1)').nextAll();

	// DOM element create -> edit -> append 
	$('<p><a>jQuery</a></p>')
	    .find('a')
	    .attr('href', 'http://www.jquery.com')
	    .end()
	    .appendTo('body');

	// remove DOM element
	$('a').remove('.someClass');

	// replace DOM element
	$('div.remove').replaceWith('<div>Removed</div>');
	$('<div>Removed</div>').replaceAll('div.remove'); // equivalent
	
	// clone DOM element
	$('div')
	    .clone()
	    .appendTo('body');

	$('div')
	    .clone(true) // preserve all events and children
	    .find()
	    .appendTo()
	    .end()
	    .end()
	    .remove();

	// getting and setting 
	$('div')
	    .attr('name','value') // setting
	    .attr('name');        // getting

	// manipulate HTML content
	$('p')
	    .html('<h1>content</h1>') // innerHTML
	    .html();

	// manipulate text
	$('p')
	    .text('<h1>content</h1>') // will auto-escape
	    .text();

    });



})(jQuery);
