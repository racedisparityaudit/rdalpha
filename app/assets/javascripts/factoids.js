function init(){


  console.log($("button"))
  function applyFilters(e){
    e.preventDefault()
    var selectedTopics = $("input",".options-container").filter(function(i,e){ return e.checked})
    $('.row-container').hide()
      selectedTopics.each(function(i,topic){
        console.log(topic)
      var klass = "." + topic.name.split(" ")[0]
      $(klass).show()
    })

  }

  $("button").on("click",applyFilters)
  //TODO remove hack - should just work with frontend toolkit
  $(".selection-button-radio").click(function(e){
    $(".selection-button-radio").removeClass("selected")
    $(e.currentTarget).addClass("selected")
  })
}

$(document).ready(init)
$(document).on('turbolinks:load', init)

function test(){
  console.log("test")
}

$(document).ready(test)
$(document).on('turbolinks:load', test)
