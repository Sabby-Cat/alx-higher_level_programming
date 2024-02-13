#!/usr/bin/node
let nrg = 0;

exports.logMe = function (item) {
  console.log(nrg + ': ' + item);
  nrg++;
};
