/* eslint-disable no-unused-vars */
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

export const createUser = async (firstName, lastName, email, password) => {
    try {
        const userName = firstName.concat(' ', lastName);
        let newUser = await client.addUser([userName, email, password])
        if (newUser !== 'User Added!!') return
        return newUser
    } catch (error) {
        return
    }
};

export const loginUser = async (email, password) => {
    let userData = await client.userValidation([email, password])
    if (userData === "User Not Found!!") return
    if (userData === "Error while doing the Operation!!") return "Something went wrong"
    return userData 
};

export const getUser = async (userId) => {
    return;
};

export const createPassword = async (accountName, accountUrl, email, Password, userId) => {
    let newPassword = await client.addCreate([accountName, accountUrl, email, Password, userId])
    if (newPassword === "Credentails Present!!") return 'Credentails Present!!'
    if (newPassword === "Error while doing the Operation!!") return "Something went wrong"
    return newPassword
};


export const getPasswordsByUserID = async id => {
    return;
};

export const getPassword = async id => {
    return;
};

export const updatePassword = async (payload, id) => {
    return;
};

export const deletePassword = async id => {
    return;
};