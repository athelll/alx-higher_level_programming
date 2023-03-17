#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const x = ++number;
  theFunction(x);
};
