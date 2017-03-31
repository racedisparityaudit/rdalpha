
(function(){
  function prototype(){
    $(".breakdown-controller").click(function(event) {
      var target = $( event.target )
      $('.' + target.attr('data-target')).toggleClass('js-hidden');
      $('#triangle-' + target.attr('data-target')).toggleClass('rotate');
    });
  }

  $(document).on('turbolinks:load', prototype)
})()