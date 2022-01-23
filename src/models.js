/* eslint-disable no-undef */
var client = require('./client.js');
var kill = require('tree-kill');

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

function test(params) {
    for (var i = 0; i < params.length; i++) {
        console.log(params[i]);
    }
}

function start() {
    globalThis.subpy = require('child_process').spawn('./server.exe')
}

export const createUser = async (firstName, lastName, email, password) => {
    try {
      let newUser = await client.query(
      q.Create(
        q.Collection('users'),
          {
            data: {
              firstName, 
              email, 
              lastName, 
              password
            }
          }
        )
      )
      if (newUser.name === 'BadRequest') return
      newUser.data.id = newUser.ref.value.id
      return newUser.data
    } catch (error) {
      return
    }
  }