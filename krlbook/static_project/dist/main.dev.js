"use strict";

$(document).ready(function () {
  $('.modal-profile').modal('hide');
  $('#modal-btn').click(function () {
    $('.modal-profile').modal('show');
  });
  $('.ui.dropdown').dropdown();
  var display = false;
  $(".comment-box").hide(500);
  $(".cmt_btn").click(function () {
    console.log('a');

    if (display === false) {
      $(this).next(".comment-box").show("slow");
      display = true;
    } else {
      $(this).next(".comment-box").hide("slow");
      display = false;
    }
  });
});