$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.fixed-action-btn').floatingActionButton();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });