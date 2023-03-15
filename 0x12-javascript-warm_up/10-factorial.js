#!/usr/bin/node

const a = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }

  return num * factorial(num - 1);
}

const result = factorial(a);
console.log(result);
