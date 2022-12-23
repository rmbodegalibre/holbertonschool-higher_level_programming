#!/usr/bin/node
// This script fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles are listed in the HTML tag UL#list_movies
// It doesn't use document.querySelector to select the HTML tag
// It uses the JQuery API
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (let i = 0; 1 < data.results.length; i++) {
    $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
