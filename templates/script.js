$(document).ready(function() {
  $(".delete-btn").click(function() {
    var configId = $(this).data("id");
    $.ajax({
      url: "/configs/" + configId,
      type: "DELETE",
      success: function(result) {
        // Обновляем страницу после успешного удаления конфигурации
        location.reload();
      },
      error: function(xhr, status, error) {
        // Выводим ошибку удаления конфигурации
        alert("Error deleting config: " + xhr.responseText);
      }
    });
  });
});
