// LOGIN TABS
$(function () {
    var tab = $('.tabs h3 a');
    tab.on('click', function (event) {
        event.preventDefault();
        tab.removeClass('active');
        $(this).addClass('active');
        tab_content = $(this).attr('href');
        $('div[id$="tab-content"]').removeClass('active');
        $(tab_content).addClass('active');
    });
});

// SLIDESHOW
$(function () {
    $('#slideshow > div:gt(0)').hide();
    setInterval(function () {
        $('#slideshow > div:first')
            .fadeOut(500)
            .next()
            .fadeIn(500)
            .end()
            .appendTo('#slideshow');
    }, 3500);
});

// DISPLAY MSSG
$(function () {
    $('.recovery .button').on('click', function (event) {
        event.preventDefault();
        $('.recovery .mssg').addClass('animate');
        setTimeout(function () {
            $('.recovery').swapClass('open', 'closed');
            $('#toggle-terms').swapClass('open', 'closed');
            $('.tabs-content .fa').swapClass('active', 'inactive');
            $('.recovery .mssg').removeClass('animate');
        }, 1300);
    });
});

// DISABLE SUBMIT FOR submission - testing purpose
// $(function () {
//     $('.button').on('click', function (event) {
//         $(this).stop();
//         event.preventDefault();
//         return false;
//     });
// });