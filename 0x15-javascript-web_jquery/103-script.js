$(function () {
  $('#btn_translate').click(function () {
    translate();
  });

  $('#language_code').keypress(function (event){
    if (event.keyCode === 13) {
      translate();
    }
  });

  function translate () {
    const code = $('#language_code').val();
    const api = 'https://hellosalut.stefanbohacek.dev/';
    if (code !== '') {
      $.get(api, { lang: code }, function (data, status, xhr) {
        if (status === 'success') {
          $('#hello').text(data.hello).css('color', '#FFFFFF');
        } else {
          $('#hello').text('error getting translation status code: ' + xhr.status);
        }
      });
    } else {
      $('#hello').text('space cannot be empty, input code').css('color', '#FF0000');
    }
  }
});
