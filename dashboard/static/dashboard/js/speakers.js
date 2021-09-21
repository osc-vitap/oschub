$(".slider").owlCarousel({
  loop: true,
  autoplay:true,
  autoplayTimeout: 2000,
  autoplayHoverPause: true,
  dots:true,
  responsiveClass:true,
  responsive:
  {
    0:
    {
      items:1,
      nav:false,
    },
    1200:{
      items:3,
    }
  }
})
