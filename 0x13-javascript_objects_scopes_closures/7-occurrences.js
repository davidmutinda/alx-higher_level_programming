#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter((val) => val === searchElement);
  return newList.length;
};
