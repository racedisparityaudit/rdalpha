(function(){

  function init(){
    new GOVUK.SelectionButtons();

    $(".radios-container").hide()
    $("#homepage-navigation-tabs span").on("click", function(e) {
          e.preventDefault()
          $(".radios-container").hide()
          var section_id =  "#" + this.id.split("-")[0] + "-radios"
          $(section_id).toggle()
        }
      )

    $("#topic-selector").trigger("click")
  }

  $(document).ready(init)
  $(document).on('turbolinks:load', init)
}())
