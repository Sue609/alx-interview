#!/usr/bin/node

const req = require('request');

req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  order(actors, 0);
});
const order = (actors, x) => {
  if (x === actors.length) return;
  req(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    order(actors, x + 1);
  });
};
