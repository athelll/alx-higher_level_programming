#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  const str = 'X'.repeat(x);
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
