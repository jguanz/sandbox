(function(window) {
  console.log("Include view.js");

  function View(){
    console.log("Instantiated view.js")
  }

  // Export to window
  window.app = window.app || {};
	window.app.View = View;
})(window);
