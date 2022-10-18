#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) console.log(error);

  // console.log(body);

  fs.writeFile(path, body, 'utf-8', error => {
    if (error) console.log(error);
  });
});
