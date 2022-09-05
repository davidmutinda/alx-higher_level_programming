#!/usr/bin/node
const array = process.argv;
if (array.length < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
