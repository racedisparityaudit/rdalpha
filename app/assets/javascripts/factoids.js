function init(){

  $("#filter-button").on("click",applyFilters)

  console.log($(".button"))
  function applyFilters(e){
    var selectedTopics = $("input",".options-container").filter(function(e){ return e.checked})
    console.log(selectedTopics)
    console.log("called")

  }

  //TODO remove hack - should just work with frontend toolkit
  $(".selection-button-radio").click(function(e){
    $(".selection-button-radio").removeClass("selected")
    $(e.currentTarget).addClass("selected")
  })
}

$(document).ready(init)
$(document).on('turbolinks:load', init)
