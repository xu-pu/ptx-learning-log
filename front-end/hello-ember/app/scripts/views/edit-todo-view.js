/*global Todos, Ember */
(function(){

    'use strict';

    Todos.EditTodoView = Ember.TextField.extend({

	focusOnInsert: function(){
	    this.$().val(this.$().val());
	    this.$().focus();
	}.on('didInsertElement')

    });

    Ember.Handlebars.helper('edit-todo', Todos.EditTodoView);
    
}());
