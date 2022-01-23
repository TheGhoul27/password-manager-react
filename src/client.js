var xmlrpc = require('xmlrpc')

// var subpy = require('child_process').spawn('./server.exe')
var subpy = require('child_process').spawn('python', ['Password-Manager.py'])

var client = xmlrpc.createClient({ host: 'localhost', port: 5050, path: '/'})

// Sends a method call to the XML-RPC server
client.methodCall('addUser', ['Pradhumna', 'pradhumna2001@gmail.com', 'pradhumna'], function (error, value) {
  // Results of the method response
  // console.log('Method response for \'anAction\': ' + value)
  console.log(error)
  if (error === null) {
    console.log('User Created!!' + value)
  }
  else {
    console.log('Error while creating User!!')
  }
});

client.methodCall('userValidation', ['Pradhumna', 'pradhumna'], function (error, value) {
  if (error === null) {
    console.log(value)
  }
  else {
    console.log('User not Found')
  }
})