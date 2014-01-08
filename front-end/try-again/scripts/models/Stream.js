define([
    'relational',
    'models/Feed',
    'models/Feeds',
    'models/Category',
], function (Relational, Feed, Feeds, Category) {

    'use strict';
    
    var Stream = Relational.RelationalModel.extend({

	relations: [
	    {
		key: 'feeds',
		type: 'HasMany',
		relatedModel: Feed,
		collectionType: Feeds,
		reverseRelation: {
		    key: 'stream',
		}
	    },
	    {
		key: 'category',
		type: 'HasOne',
		relatedModel: Category,
		reverseRelation: {
		    key: 'streams',
		    type: 'HasMany',
		}
	    }],

	initialize: function(){},

	isReady: function(){},

	getReady: function(){},

	fetch: function(){},

    });

    return Stream;

});
