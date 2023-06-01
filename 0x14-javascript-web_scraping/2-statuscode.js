#!/usr/bin/node

const url = process.argv[2];
const rq = require('request');
rq(url, function (error, response, body) {
  if (error) throw error;
  console.log('code:', response && response.statusCode);
});
