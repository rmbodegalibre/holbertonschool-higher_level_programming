#!/usr/bin/node
// This script adds the class red to the <header> element when the user clicks on the tag DIV#red_header
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
});
