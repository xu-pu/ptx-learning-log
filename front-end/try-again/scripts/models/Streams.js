define([
    'backbone',
    'models/Stream',
], function (Backbone, Stream) {

    'use strict';

    var Streams = Backbone.Collection.extend({
	model: Stream
    });

    return Stream;

});
