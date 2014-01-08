define([
    'models/Feed',
    'models/Stream',
    'models/Category',
] ,function (Feed, Stream, Category) {
    
    'use strict';

    return function () {

	var feed1 = new Feed({ message: 'something 1' });
	var feed2 = new Feed({ message: 'something 2' });
	var feed3 = new Feed({ message: 'something 3' });

	var myCategory = new Category({ name: 'my category'})

	var firstStream = new Stream({ 
	    name: 'first one', 
	    feeds: [ feed1, feed3 ],
	    category: myCategory,
	});

	var secondStream = new Stream({ 
	    name: 'second one',
	    feeds: [ feed2 ],
	    category: myCategory,
	});
	
	console.log(firstStream.get('feeds').pluck('message'));

	console.log(myCategory.get('streams').pluck('name'));

    };

});
