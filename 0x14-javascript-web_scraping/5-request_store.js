#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const rq = require('request');
const writer = require('fs');

rq(url, function (err, response, body) {
  if (err) {
    // handles error
    throw err;
  } else if (response.statusCode === 200) {
    // writes into file
    writer.writeFile(file, body, 'utf8', function (err) {
      // handles error
      if (err) throw err;
    });
    // handles error
  } else {
    console.log('error: ', response.statusCode);
  }
});
