#!/usr/bin/node
// This script updates the text color of the < header > element to red(#FF0000) when the user clicks on the tag DIV#red_header:
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$('DIV#red_header').click(function () {
    $('HEADER').css('color', '#FF0000');
});
