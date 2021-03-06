/**
 * Created by avtan on 22.02.2017.
 */


function Show() {
    $(this).parent('.sub_menu').siblings('a').addClass('hover_link');
}

function Hide() {
    $(this).parent('.sub_menu').siblings('a').removeClass('hover_link');
}

$(document).ready(function () {
    var menu = $(".sub_menu li");

    menu.on('mouseover', Show);
    menu.on('mouseout', Hide);

    $('.slider_news').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 6000,
        infinite: true,
        arrows: true,
        variableWidth: true,
        draggable: false
    });
});

$('.tabs-stage > div').hide();
$('.tabs-stage > div:nth-child(1)').show();
$('.tabs-nav > li:first-child a').addClass('tab-active');

// �������� ����� ������� � ���������� ����������
$('.tabs-nav > li > a').on('click', function (event) {
    event.preventDefault();
    $('.tabs-nav > li a').removeClass('tab-active');
    $(this).addClass('tab-active');
    $('.tabs-stage > div').hide(500);
    $($(this).attr('href')).show(500);
});

$(".item").magnificPopup({
    type: 'image',
    gallery: {
        enabled: true
    }
});