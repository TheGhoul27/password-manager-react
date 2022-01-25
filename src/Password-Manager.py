from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from pythonScripts.managePassword import *
from cryptography.fernet import Fernet
import sqlite3

conn = sqlite3.connect('password_manager.db')

try:
    conn.execute(
        """CREATE TABLE USERS(USERNAME TEXT, MAIL TEXT, PASSWORD TEXT)""")

except:
    cursor = conn.execute("SELECT * from USERS")


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        generate_key()
        return open("secret.key", "rb").read()


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2', '/')


# class mainOperations:

def add_create(addorCreate, service, username, password):
    update_or_not = functionCallAdd(
        addorCreate, service, username, password, load_key(), conn)
    return update_or_not


def others(function, service, username):
    functionCallOthers(function, service, username, load_key(), conn)


def getUsernames(user):
    return getAll(user, load_key(), conn)


def addUser(username, mail, password):
    alreadyThere = createUser(username, mail, password, load_key(), conn)
    return alreadyThere


def userValidation(username, password):
    flag = checkUser(username, password, load_key(), conn)
    return flag


def forgotPassword(username):
    forgot(username, load_key(), conn)


if __name__ == '__main__':
    server = SimpleXMLRPCServer(
        ("localhost", 5050), requestHandler=RequestHandler)
    server.register_introspection_functions()
    # server.register_instance(mainOperations())

    server.register_function(add_create, 'addCreate')
    server.register_function(others, 'others')
    server.register_function(getUsernames, 'get')
    server.register_function(addUser, 'addUser')
    server.register_function(userValidation, 'userValidation')
    server.register_function(forgotPassword, 'forgotPassword')
server.serve_forever()
