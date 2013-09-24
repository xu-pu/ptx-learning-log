//==========================================================================
// <jQuery Cookbook> Chapter #2 -- selecting elements with jQuery
//==========================================================================

(function($){
    $(document).ready(function(){
	
	// child selector
	var anchors = $('#nav li > a'); // only the direct children of (#nav li) are selected
	anchors.children('p');
	$('> *', anchors); // left side of > can be empty if context is specified

	// sibling selector
	$('h1').siblings('h1,h2,h3,p');
	$('li.selected').nextAll('li');
	$('li.selected').next('li');
	$('li.selected ~ li');

	// index selector
	$('li:first');
	$('li:last');
	$('li:even');
	$('li:odd');
	// eq, lt, gt index start from 0
	$('li:eq(0)'); // index equal n
	$('li:lt(n)'); // index less than n 
	$('li:gt(n)'); // index greater than n 

	// animating elements
	$('div:animated');

	// select by content
	$('div:contains("text")');
	$('div:has(li a)')
	$('p').filter(function(){
	    return /regex/.test($(this).text());
	});

	// exclude selector
	$('div:not(#someid)');
	$('a:not(div.important a, a.nav)');
	$('some selector').not('selector'); 

	// select by visibility
	$('div:hidden');
	$('div:visible').hide();

	// select by attribute
	$('a[attr]'); // have attr
	$('a[attr="value"]');
	$('a[attr!="value"]');
	$('a[attr^="value"]'); // start with
	$('a[attr$="value"]'); // end with
	$('a[attr~="value"]'); // with space at head and tail

	// select form elements by type
	$('input:text,password')
	
	// programmatic filter 
	$('div').filter(function(){
	    return true; // include
	});

	// context parameter
	$('form').bind('submit', function(){
	    var inputs = $('input', this); // in the context of 'this'
	});

	$('context').find('selector');

	// creating customized selecors
	$.expr[':'].myFilter = function(elem, index, m){return true;};
	$('a').filter(':not(:myFilter)');

    });
})(jQuery);
