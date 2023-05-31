$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    dataType: "json",
    success: function(data) {
      var helloTranslation = data.hello;

      $("#hello").text(helloTranslation);
    },
    error: function() {
      console.log("Error fetching translation data.");
    }
  });
});
