#!/usr/bin/node
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  const movie = JSON.parse(body).title;
  console.log(movie);
});
