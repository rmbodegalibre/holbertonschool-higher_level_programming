#!/usr/bin/node
// This script prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the movie ID
// It uses the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
// It uses the module request
const reqTitle = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
reqTitle(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
