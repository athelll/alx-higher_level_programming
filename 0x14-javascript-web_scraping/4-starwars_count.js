#!/usr/bin/node

const url = process.argv[2];
const rq = require('request');

// makes request
rq(url, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    // parses response to json if successfull
    const films = JSON.parse(body).results;
    let count = 0;
    // iterates over films
    for (const film of films) {
      const characters = film.characters;
      // iterates over characters in films
      for (const c of characters) {
        if (c.includes('18')) {
          // updated count
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('error: ', response.statusCode);
  }
});
