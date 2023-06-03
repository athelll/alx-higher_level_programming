 $(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
    if (status === 'success') {
      $('#hello').text(data.hello);
    }
  });
});

// tried to handle the redirection here
// but got CORS error that bugged me for a while
/**
$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    method: "GET",
    crossDomain: true,
    xhrFields: { withCredentials: true },
    success: function(data, status, xhr) {
      if (xhr.status === 301 || xhr.status === 302) {
        const redirect = xhr.getResponseHeader('Location');
        $.get(redirect, function () {
          $("#hello").text(data.hello);
        });
      }
    },
    error: function() {
      $("#hello").text("Failed to fetch translation.");
    }
  });
});
**/
