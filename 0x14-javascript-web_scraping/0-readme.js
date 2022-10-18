#!/usr/bin/node

const fs = require('fs');
const file = process.argv;

fs.readFile(file[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
