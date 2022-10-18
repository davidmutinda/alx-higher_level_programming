#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';

request(url, (error, response, body) => {
  if (error) console.log(error);
  let number = 0;
  const episodes = JSON.parse(body).results;
  episodes.forEach(el => {
    el.characters.forEach(n => {
      if (n.includes(id)) number++;
    });
  });

  console.log(number);
});
