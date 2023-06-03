$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
    if (status === 'success') {
      for (film of data.films) {
        $.get(film, function (resp, status) {
          $('ul#list_movies').append('<li>'+ resp.title +'</li>');
        });
      }
    }
  });
});
