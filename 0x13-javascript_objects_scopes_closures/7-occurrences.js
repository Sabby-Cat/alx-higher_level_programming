#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    const rdc = function (count, val) {
      count += (val === searchElement) ? 1 : 0;
      return count;
    };
    return list.reduce(rdc, 0);
  };
