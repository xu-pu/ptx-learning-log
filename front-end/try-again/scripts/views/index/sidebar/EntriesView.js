define([

], function () {

    'use strict';

    var EntriesView = Marionette.CollectionView.extend({

	className: 'sidebar-entries',
	
	itemView: EntryView,

    });

});
