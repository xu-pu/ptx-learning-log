define([
    'jquery',
    'backbone'
], function($, Backbone) {

    var TabView = Backbone.View.extend({

        events: {
            'click .sidebar-tab': 'toggleTab',
        },

        initialize: function() {
            this.$tab = $('.sidebar-tab', this.$el);
            this.$body = $('.sidebar-tab-body', this.$el);

            this.$body.hide();
            this.active = false;

        },

        toggleTab: function() {
            if (this.active) {
                this.active = false;
                this.$body.stop(true, true).slideUp('normal')
            } else {
                this.active = true;
                this.$body.filter(':visible').slideUp('normal');
                this.$body.stop(true, true).slideDown('normal');
            }
        }

    });

    return TabView;

});
