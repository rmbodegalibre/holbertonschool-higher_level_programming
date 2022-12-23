#!/usr/bin/node
// This script updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
