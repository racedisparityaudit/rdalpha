console.log("helloworld");
(function(){
  function prototype(){
    $(".breakdown-controller").click(function(event) {
      console.log('click');
      var target = $( event.target )
      console.log(target);
      $('.' + target.attr('data-target')).toggleClass('js-hidden');
    });
  }

  $(document).on('turbolinks:load', prototype)
})()