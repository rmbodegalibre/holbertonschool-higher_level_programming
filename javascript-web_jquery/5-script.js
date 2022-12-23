#!/usr/bin/node
// This script adds a <li> element to a list when the user clicks on the tag DIV#add_item:
// The new element is: <li>Item</li>
// The new element is added to UL.my_list
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$('DIV#add_item').click(function () {
  $('ul.my_list').append('<LI>Item</LI>');
});
