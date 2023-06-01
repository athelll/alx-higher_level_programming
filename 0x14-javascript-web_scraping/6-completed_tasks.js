#!/usr/bin/node

const api = process.argv[2];
const request = require('request');

request(api, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const result = {};
    const data = JSON.parse(body);
    for (const d of data) {
      if (d.completed === true) {
        if (result[d.userId] === undefined) {
          result[d.userId] = 1;
        } else {
          result[d.userId]++;
        }
      }
    }
    console.log(result);
  } else {
    console.log('error: ', response.statusCode);
  }
});
