define([
    'relational'
], function (Relational) {

    'use strict';

    var Job = Relational.RelationalModel.extend({
	defaults: {
	    'startDate': null,
	    'endDate': null
	}
    });

    var Person = Relational.RelationalModel.extend({
	relations: [{
	    type: 'HasMany',
	    key: 'jobs',
	    relatedModel: Job,
	    reverseRelation: {
		key: 'person'
	    }
	}]
    });

    var Company = Relational.RelationalModel.extend({
	relations: [{
	    type: 'HasMany',
	    key: 'employees',
	    relatedModel: Job,
	    reverseRelation: {
		key: 'company'
	    }
	}]
    });

});
