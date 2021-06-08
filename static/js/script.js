$(document).ready(function(){
  // Navbar
  var elems_navbar = document.querySelectorAll('.sidenav');
  var options_navbar = {
    edge: 'right'
  };
  var instances_navbar = M.Sidenav.init(elems_navbar, options_navbar);
  // Select form
  var elems_select = document.querySelectorAll('select');
  var instances_select = M.FormSelect.init(elems_select);
  // Tooltip
  var elems_tooltip = document.querySelectorAll('.tooltipped');
  var instances_tooltip = M.Tooltip.init(elems_tooltip);
  // Collapsible
  var elems_collapsible = document.querySelectorAll('.collapsible');
  var instances_collapsible = M.Collapsible.init(elems_collapsible);
  // Tabs
  var elems_tabs = document.querySelectorAll('.tabs');
  var instance_tabs = M.Tabs.init(elems_tabs);
  // Modals
  var elems_modal = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems_modal);
  // Datepicker
  var elems_datepicker = document.querySelectorAll('.datepicker');
  var option_datepicker = {
    format: "dd mmmm, yyyy",
    yearRange: 3,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  };
});