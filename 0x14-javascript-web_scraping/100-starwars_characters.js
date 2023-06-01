#!/usr/bin/node

const id = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(api, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const links of characters) {
      request(links, function (err, response, body) {
        if (err) console.log(err);
        console.log(JSON.parse(body).name);
      });
    }
  } else {
    console.log('error: ', response.statusCode);
  }
});
