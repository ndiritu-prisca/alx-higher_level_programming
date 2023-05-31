$(document).ready(function() {
  $("#btn_translate").click(function() {
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
  });
});
