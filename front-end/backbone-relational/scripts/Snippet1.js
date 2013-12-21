define([
    'relational'
], function (Relational) {

    'use strict';

    var Animal = Relational.RelationalModel.extend({
	urlRoot: '/animal/'
    });

    var AnimalCollection = Relational.Collection.extend({
	model: Animal
    });

    var Zoo = Relational.RelationalModel.extend({
	relations: [{
	    type: 'HasMany',
	    key: 'animals',
	    relatedModel: Animal,
	    collectionType: AnimalCollection,
	    reverseRelation: {
		key: 'livesIn',
		includeInJSON: 'id'
	    }
	}]
    });

    return function() {
	var artis = new Zoo({ name: 'Artis' });
	var lion = new Animal({ species: 'Lion', livesIn: artis });

	console.log( artis.get('animals').pluck('species') );

	console.log( lion.get('livesIn').get('name') );

	var amersfoort = new Zoo({ name: 'Dierenpark Amersfoort', animals: [ lion ] });

	console.log( lion.get('livesIn').get('name') );

    };

});
