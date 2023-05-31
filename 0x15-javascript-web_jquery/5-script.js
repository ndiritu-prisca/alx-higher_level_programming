$(document).ready(function() {
  $("#add_item").click(function() {
    var newItem = $("<li>").text("Item");

    $("ul.my_list").append(newItem);
  });
});
