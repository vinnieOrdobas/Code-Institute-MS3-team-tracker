$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('select').formSelect();
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    $('.tabs').tabs();
    $('.modal').modal();
    $('select').formSelect();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
    $('ul.tabs').tabs();
  });