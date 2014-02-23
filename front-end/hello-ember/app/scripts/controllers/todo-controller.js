/*global Todos, Ember */
(function(){

    'use strict';

    Todos.TodoController = Ember.ObjectController.extend({
	
	isEditing: false,
	
	bufferedTitle: Ember.completed.oneWay('title'),

	actions: {
	    editTodo: function(){
		this.set('isEditing', true);
	    },

	    doneEditing: function(){
		var bufferedTitle = this.get('bufferedTitle').trim();
		if (Ember.isEmpty(bufferedTitle)) {
		    Ember.run.debounce(this, 'removeTodo', 0);
		}
		else {
		    var todo = this.get('model');
		    todo.set('title', bufferedTitle);
		    todo.save();
		}
		this.set('bufferedTitle', bufferedTitle);
		this.set('isEditing', false);
	    },

	    cancelEditing: function(){
		this.set('bufferedTitle', this.get('title'));
		this.set('isEditing', false);
	    },

	    removeTodo: function(){
		this.removeTodo();
	    }
	},

	removeTodo: function(){
	    var todo = this.get('model');
	    todo.deleteRecord();
	    todo.save();
	},

	saveWhenComputed: function(){
	    this.get('model').save();
	}.observes('isCompleted')

    });

}());
