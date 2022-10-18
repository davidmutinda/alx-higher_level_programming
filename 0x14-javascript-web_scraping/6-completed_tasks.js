#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);

  const tasks = JSON.parse(body);
  const obj = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!obj[`${task.userId}`]) {
        obj[`${task.userId}`] = 1;
      } else {
        obj[`${task.userId}`]++;
      }
    }
  });
  console.log(obj);
});
