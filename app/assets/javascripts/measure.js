(function(){
  // stop everything being called twice if loaded with turbolinks and page load.
  var initialised = false;

  function init(){
    if(initialised) return;
    $(".accordion__header").click(function(e){

        var body = $(e.currentTarget).parent().find(".accordion__body")
        $(body).toggle()

        console.log("foo")
    })
    initialised = true;

    $(".accordion__header").trigger("click")
  }

  $(document).ready(init)
  $(document).on('turbolinks:load', init)
}())
