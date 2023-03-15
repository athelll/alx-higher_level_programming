#!/usr/bin/node

// variables
let result;
let bigger;
const args = intArray(process.argv).slice(2);
const Max = Math.max(...args);

// intarray function
function intArray (arr, a, b) {
  const newarr = [];

  for (const x of arr) {
    newarr.push(parseInt(x));
  }
  return newarr;
}

// checkers
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else if (args.length === 2) {
  const result = args[0] <= args[1] ? args[0] : args[1];
  console.log(result);
} else {
// algorithm
  for (const x of args) {
    if (x === Max) {
      continue;
    }

    for (const a of args) {
      if (a === Max || a === x) {
        continue;
      }

      if (x > a) {
        bigger = true;
      } else {
        bigger = false;
        break;
      }
    }

    if (bigger === true) {
      result = x;
      break;
    }
  }

  // result
  console.log(result);
}
