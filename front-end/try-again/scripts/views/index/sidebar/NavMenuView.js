define([

], function () {

    'use strict';

    var NavigationMenuView = Marionette.CollectionView.extend({

	itemView: SubMenuView,

    });

    return NavigationMenuView;

});
