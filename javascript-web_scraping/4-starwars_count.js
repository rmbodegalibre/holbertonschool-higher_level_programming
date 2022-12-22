#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18 - this script uses this ID for filtering the result of the API
// It uses the module request
const reqCount = require('request');
reqCount(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
