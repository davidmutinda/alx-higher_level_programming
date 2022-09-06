#!/usr/bin/node

const fs = require('fs');

let data;
fs.readFile('./fileA', 'utf-8', (err, d) => {
  if (err) {
    console.error(err);
    return;
  }
  data = d;
  fs.readFile('./fileB', 'utf-8', (err, d) => {
    if (err) throw err;
    data += d;
    fs.writeFile('./fileC', data, (err) => {
      if (err) throw err;
    });
  });
});
