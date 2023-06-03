$(function () {
  $('#add_item').click(() => {
    $('ul.my_list').append($('<li></li>').text('item'));
  });
});
