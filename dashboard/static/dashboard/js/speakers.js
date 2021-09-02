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
          600:
          {
            items:1,
            nav:false,
          },
          1000:
          {
            items:3,
            nav:false,
          }
        }
})
