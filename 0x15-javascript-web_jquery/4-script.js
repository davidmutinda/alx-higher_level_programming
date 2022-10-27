$('div#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
        $('header').removeClass('green');
        $('header').attr('class', 'red');
    } else {
        $('header').removeClass('red');
        $('header').attr('class', 'green');
    }
});