/* eslint-disable no-undef */
/* Access-Control-Allow-Origin */
var xmlrpc = require('xmlrpc');
/* var kill = require('tree-kill');
const { PythonShell } = require('python-shell');
const path = require('path'); */

//var {spawn} = require('child_process')

/* function start() {
  //globalThis.subpy = spawn('python', ['./Password-Manager.py'])
  let pyshell = new PythonShell(path.join(__dirname, './Password-Manager.py'), {
    pythonPath: 'python3',
});
  //sleep(1000);
  //globalThis.subpy = require('child_process').spawn('./server.exe')
  globalThis.client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
} */

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
      currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

// sleep(1000);


// Sends a method call to the XML-RPC server

function quitUser() {
  //start();
  sleep(1000);
  client.methodCall('quitUser', [], function (error, value) {
    // Results of the method response
    // console.log('Method response for \'anAction\': ' + value)
    if (error === null) {
      console.log('User Logged Out!!');
      // kill(subpy.pid);
      return 'User Logged Out';
    }
    else {
      console.log(error);
      console.log('Error while doing the Operation!!');
      // kill(subpy.pid);
      return 'Error';
    }
  });
}

function addUser(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/'});
  return new Promise(function (resolve, reject) {
    return client.methodCall('addUser', params, function (error, value) {
      if (error === null) {
        if (value === true) {
          console.log('User Added!!');
          // kill(subpy.pid);
          return resolve('User Added!!');
        }
        else {
          console.log('User Already Exists!!');
          // kill(subpy.pid);
          return resolve('User Already Exists!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  });
}


function userValidation(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
  return new Promise(function (resolve, reject) {
    return client.methodCall('userValidation', params, function (error, value) {
      if (error === null) {
        if (value === true) {
          console.log('User Found!!');
          // kill(subpy.pid);
          return resolve('User Found!!');
        }
        else {
          console.log('User Not Found!!');
          // kill(subpy.pid);
          return resolve('User Not Found!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  }
  );
}

function addCreate(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
  return new Promise(function (resolve, reject) {
    return client.methodCall('addCreate', params, function (error, value) {
      if (error === null) {
        if (value === true) {
          console.log('Credentails Added!!');
          // kill(subpy.pid);
          return resolve('Credentails Added!!');
        }
        else {
          console.log('Credentails Present!!');
          // kill(subpy.pid);
          return resolve('Credentails Present!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  }
  );
}

function others(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
  return new Promise(function (resolve, reject) {
    return client.methodCall('others', params, function (error, value) {
      if (error === null) {
        if (value === true) {
          console.log('Operation Done!!');
          // kill(subpy.pid);
          return resolve('Operation Done!!');
        }
        else {
          console.log('Operation Aborted!!');
          // kill(subpy.pid);
          return resolve('Operation Aborted!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  }
  );
}

function forgotPassword(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
  return new Promise(function (resolve, reject) {
    return client.methodCall('forgotPassword', params, function (error, value) {
      if (error === null) {
        if (value === true) {
          console.log('Password Sent!!');
          // kill(subpy.pid);
          return resolve('Password Sent!!');
        }
        else {
          console.log('User Not Found!!');
          // kill(subpy.pid);
          return resolve('User Not Found!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  }
  );
}

function get(params) {
  /* start();
  sleep(1000); */
  client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/' });
  return new Promise(function (resolve, reject) {
    return client.methodCall('get', params, function (error, value) {
      if (error === null) {
        if (value !== null) {
          console.log('Password Found!!');
          // kill(subpy.pid);
          return resolve(value);
        }
        else {
          console.log('Password Not Found!!');
          // kill(subpy.pid);
          return resolve('Password Not Found!!');
        }
      }
      else {
        console.log('Error while doing the Operation!!');
        // kill(subpy.pid);
        return reject(error);
      }
    });
  });
}


module.exports = { addUser, userValidation, addCreate, others, forgotPassword, get, quitUser };

// Website to make one big function to access all the functions: https://getstream.io/blog/javascript-promises-and-why-async-await-wins-the-battle/ 