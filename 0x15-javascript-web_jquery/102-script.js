$(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val(); 
    if (code !== '') {
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + code, function (data, status, xhr) {
        if (status === 'success') {
          $('#hello').text(data.hello);
        } else {
          $('#hello').text('error getting translation status code: ' + xhr.status);
        }
      });
    } else {
      $('#hello').text('Not a Valid language code').css('color', '#FF0000');
    }
  });
});
