#!/usr/bin/node

const fs = require('fs');
const array = process.argv;

fs.writeFile(array[2], array[3], 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
