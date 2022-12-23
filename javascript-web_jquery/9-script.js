#!/usr/bin/node
// This script fetches from https://stefanbohacek.com/hellosalut/?lang=fr and
// displays the value of hello from that fetch in the HTML tag DIV#hello.
// The translation of “hello” is displayed in the HTML tag DIV#hello
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
// It works when it is imported from the <head> tag
$('document').ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
