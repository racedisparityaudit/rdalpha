(function(){

  function initFactoids(){


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

    $("button").on("click", applyFilters)

  }

  $(document).ready(initFactoids)
  $(document).on('turbolinks:load', initFactoids)
}())
