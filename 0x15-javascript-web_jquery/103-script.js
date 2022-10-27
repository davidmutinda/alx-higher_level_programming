$(document).ready(() => {
    $('#btn_translate').click(() => {
        // console.log($('#language_code').val());
        const getCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/?lang=${getCode}`;
        $.get(url, data => {
            $('#hello').text(data.hello)
        });
    });
    $('#language_code').keypress((e) => {
        if (e.which === 13) {
            const getCode = $('#language_code').val();
            const url = `https://www.fourtonfish.com/hellosalut/?lang=${getCode}`;
            $.get(url, data => {
                $('#hello').text(data.hello)
            });
        }
    });
});