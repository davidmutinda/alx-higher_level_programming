#!/usr/bin/node

const array = process.argv;
const i = array.length;

if (array.length < 4) {
  console.log(0);
} else {
  array.sort();
  console.log(parseInt(array[i - 2]));
}
