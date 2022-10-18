#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) console.log(error);

  const characters = JSON.parse(body).characters;

  characters.forEach(char => {
    request(char, (err, resp, bdy) => {
      if (err) console.log(err);
      console.log(JSON.parse(bdy).name);
    });
  });
});
