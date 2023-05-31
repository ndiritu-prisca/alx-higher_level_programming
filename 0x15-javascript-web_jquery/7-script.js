$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    success: function(data) {
      var name_char = data.name;

      $("#character").text(name_char);
    },
    error: function() {
      console.log("Error fetching character data.");
    }
  });
});
