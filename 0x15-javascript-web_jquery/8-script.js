$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: "json",
    success: function(data) {
      var movieTitles = data.results.map(function(movie) {
        return movie.title;
      });

      var listItems = movieTitles.map(function(title) {
        return $("<li>").text(title);
      });

      $("#list_movies").append(listItems);
    },
    error: function() {
      console.log("Error fetching movie data.");
    }
  });
});
