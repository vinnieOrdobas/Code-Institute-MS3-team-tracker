$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    var elems_select = document.querySelectorAll('select');
    var instances_select = M.FormSelect.init(elems_select);
    var elemsCarousel = document.querySelectorAll('.carousel');
    var instancesCarousel = M.Carousel.init(elemsCarousel);
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    $('.tabs').tabs();
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
    $('.scrollspy').scrollSpy()
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