#!/usr/bin/node

if (process.argv[0] === null || process.argv[1] === null) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
