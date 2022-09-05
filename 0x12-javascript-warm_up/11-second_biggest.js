#!/usr/bin/node

let array = process.argv;

if (array.length < 4) {
  console.log(0);
} else {
  array = array.splice(2);
  array = array.map(Number);
  const i = array.length;
  array.sort();
  console.log(array[i - 2]);
}
