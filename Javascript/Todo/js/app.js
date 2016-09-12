(function(window){
  'use strict';
  function setView(){
    this.model = new app.Model("vanillaJS-todo");
    this.view = new app.View();
  }
  addEventListener('load', setView);
})();
