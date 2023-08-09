#!/usr/bin/node

const proc = require('process');
const request = require('request');
const args = proc.argv;
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
function main () {
  if (args.length === 3) {
    request(apiUrl + args[2], (error, resp, body) => {
      if (error === null && resp.statusCode === 200) {
        const chars = JSON.parse(body).characters;
        charObjs(chars);
      }
    });
  }
}
function charObjs (chars) {
  const rqsts = [];
  for (const e of chars) {
    rqsts[rqsts.length] = new Promise((resolve, reject) => {
      request(e, (err, resp, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  }
  Promise.all(rqsts).then((rspns) => {
    rspns.forEach(resp => {
      console.log(resp.name);
    });
  });
}

main();
