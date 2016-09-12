(function (window){
  'use strict';

  function Model(name){
    this._dbName = name;
    if(!localStorage[name]){
      var data = {
        todos: []
      };
    localStorage[name] = JSON.stringify(data);
  }
}

  Model.prototype.create = function (title, callback) {
    title = title || '';
    callback = callback || function() {};

    var newItem = {
      id: 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {var r = Math.random()*16|0,v=c=='x'?r:r&0x3|0x8;return v.toString(16);}),
      title: title.trim(),
      completed: false
    };

    this.save(newItem, callback);
  }

  Model.prototype.save = function (updateData, callback){
    var data = JSON.parse(localStorage[this._dbName]);
    var todos = data.todos;

    updateData.id
    todos.push(updateData);
    localStorage[this._dbName] = JSON.stringify(data)
  }

  Model.prototype.remove = function (id, callback){
    var data = JSON.parse(localStorage[this._dbName]);
    var todos = data.todos;

    for(var i=0; i<todos.length; i++){
      if(todos[i].id == id){
        todos.splice(i, 1);
      }
    }

    localStorage[this._dbName] = JSON.stringify(data)
  }

  window.app = window.app || {}
  window.app.Model = Model;
})(window);
