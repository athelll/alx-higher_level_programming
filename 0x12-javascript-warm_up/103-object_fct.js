#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// code
myObject.incr = function () { this.value += 1; };
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
