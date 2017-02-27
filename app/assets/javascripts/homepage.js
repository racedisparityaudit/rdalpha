(function(){

  function init(){
    new GOVUK.SelectionButtons();

    $(".topic-tabs li").on("click", function(e) {
        e.preventDefault()
        $(".graph-section").hide()
        var section_id = "#" + this.id.split("-")[0] + "-section"
        $(section_id).toggle()
        console.log(section_id)}
      )
      $("#ethnicity-selector").trigger("click")

    }
  }

  $(document).ready(init)
  $(document).on('turbolinks:load', init)
}())
