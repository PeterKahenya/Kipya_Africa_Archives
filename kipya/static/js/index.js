var currentSlide=0;
$(".kipya-slide").each(function(index) {
  var active_status=""
  index===0?active_status="active":active_status="";
  $( ".kipya-slides-pagination" ).append( "<span onclick='showSlide("+  index.toString()+")' class='dot "+active_status+"'></span>" );
});

function fadeOutCurrentSlide(){
  $('.kipya-slide:eq('+currentSlide+')').hide()
  $('.dot:eq('+currentSlide+')').removeClass("active")

  if(currentSlide+1>$('.kipya-slide').length-1){
    currentSlide=0
  }else{
    currentSlide=currentSlide+1
  }

  $('.kipya-slide:eq('+currentSlide+')').show()
  $('.dot:eq('+currentSlide+')').addClass("active")

}

function showSlide(index){
    $('.kipya-slide:eq('+currentSlide+')').hide()
    $('.dot:eq('+currentSlide+')').toggleClass("active")

    $('.kipya-slide:eq('+index+')').show()
    $('.dot:eq('+index+')').toggleClass("active")

    currentSlide=index
}

function fadeInNextSlide(){
  
}

setInterval(function(){
fadeOutCurrentSlide()
},30000)