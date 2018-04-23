$(document).ready(function () {

  $('.signup-panel').hide();

  $('#login-link').click(function (){
    $('.signup-panel').hide();
    $('.login-panel').show();
  });

  $('#signup-link').click(function (){
    $('.login-panel').hide();
    $('.signup-panel').show();
  });

});