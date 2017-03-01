(function(){

  function init(){
    new GOVUK.SelectionButtons();

    $(".radios-container").hide()
    $("#homepage-navigation-tabs li").on("click", function(e) {
          e.preventDefault()
          $("#homepage-navigation-tabs li").removeClass("selected")
          $(e.currentTarget).addClass("selected")

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
