#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, response, body) => {
  if (error) console.log(error);
  let number = 0;
  const episodes = JSON.parse(body).results;
  episodes.forEach(el => {
    if (el.characters.includes(id)) number++;
  });

  console.log(number);
});
