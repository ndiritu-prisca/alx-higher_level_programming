#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    movieData.characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, characterBody) => {
        if (error) {
          console.error(error);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
