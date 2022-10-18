#!/usr/bin/node

const request = require('request');
const id = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films';

request(url, (error, response, body) => {
  if (error) console.log(error);
  const episodes = JSON.parse(body).results;
  const episode = episodes.find((el, index) => index + 1 === id);

  if (id) console.log(episode.title);
});
