#!/usr/bin/node
// This script fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name is displayed in the HTML tag DIV#character
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
