(function(){
  function init(){

   $(".question-tabs li").on("click", function(e) {
      e.preventDefault()
      $(".graph-section").hide()
      var section_id = "#" + this.id.split("-")[0] + "-section"
      $(section_id).toggle()
      console.log(section_id)}
    )
    $("#ethnicity-selector").trigger("click")

  }
// turbo links... if you get a weird bug where it doesn't
// load the js when you navigate to it only when you refresh.
$(document).ready(init)
$(document).on('turbolinks:load', init)
})()

