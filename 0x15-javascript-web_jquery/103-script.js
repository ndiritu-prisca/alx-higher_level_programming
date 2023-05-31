$(document).ready(function() {
  $("#btn_translate").click(fetchTranslation);
  $("#language_code").keypress(function(event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    var langCode = $("#language_code").val();

    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/",
      data: { lang: langCode },
      dataType: "json",
      success: function(data) {
        var helloTranslation = data.hello;

        $("#hello").text(helloTranslation);
      },
      error: function() {
        console.log("Error fetching translation data.");
      }
    });
  }
});
