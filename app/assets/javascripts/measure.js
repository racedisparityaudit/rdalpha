(function(){
  // stop everything being called twice if loaded with turbolinks and page load.
  var initialised = false;

  function accordions(){
    $(".accordion__header").click(function(e){
        var body = $(e.currentTarget).parent().find(".accordion__body")
        $(body).toggle()
    })
    $(".accordion__body").hide()
  }

  $(document).on('turbolinks:load', accordions)
}())
