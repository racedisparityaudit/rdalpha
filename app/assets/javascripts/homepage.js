(function(){

  function init(){
    new GOVUK.SelectionButtons();

    $(".radios-container").hide()
    $("#navigation-tabs li").on("click", function(e) {

          e.preventDefault()
          $("#navigation-tabs li").removeClass("selected")
          $(e.currentTarget).addClass("selected")

          $(".graph-section").hide()
          $(".radios-container").hide()
          var section_id =  "#" + this.id.split("-")[0] + "-section"
          $(section_id).toggle()
        }
      )

    if(attainmentPage()) {
      $("#ethnicity-selector").trigger("click")
    } else {
      $("#topic-selector").trigger("click")
    }
  }

  function attainmentPage() {
    return $('#attainment').length == 1
  }

  $(document).ready(init)
  $(document).on('turbolinks:load', init)
}())
