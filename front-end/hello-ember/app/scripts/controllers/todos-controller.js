/*global Todos, Ember */
(function(){
    
    'use strict';

    Todos.TodosController = Ember.ArrayController.extend({

	actions: {
	    createTodo: function(){
		var title, todo;
		title = this.get('newTitle').trim();
		if (!title) {
		    return;
		}
		todo = this.store.createRecord('todo', {
		    title: title,
		    isCompleted: false
		});
		todo.save();
		this.set('newTitle', '');
	    },

	    clearCompleted: function(){
		var completed = this.get('completed');
		completed.invoke('deleteRecord');
		completed.invoke('save');
	    }
	},

	remaining: Ember.computed.filterBy('content', 'isCompleted', false),

	completed: Ember.computed.filterBy('content', 'isCompleted', true),
	
	allAreDone: function(key, value) {
	    if (value !== undefined) {
		this.setEach('isCompleted', value);
		return value;
	    }
	    else {
		var length = this.get('length');
		var completedLength = this.get('completed.length');
		return length > 0 && length === completedLength;
	    }
	}.property('length', 'completed.length')
	
    });

}());
