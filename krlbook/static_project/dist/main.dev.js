"use strict";

$(document).ready(function () {
  $('#modal-btn').click(function () {
    $('.ui.modal').modal('show');
  });
  $('.ui.dropdown').dropdown();
}); // $( document ).ready(function() {
//     let display = false
//     $(".comment-box").hide(500);
//     $("#cmt_btn").click(function ()
//     {
//         console.log('a')
//         if (display === false)
//         {
//             $(this).next(".comment-box").show("slow");
//             display = true
//         } else
//         {
//             $(this).next(".comment-box").hide("slow");
//             display = false
//         }
//     });
// });