#!/usr/bin/node

const file = process.argv[2];
const reader = require('fs');
reader.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
