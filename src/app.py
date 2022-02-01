from pythonScripts.managePassword import *
from cryptography.fernet import Fernet
import sqlite3
from flask import Flask, jsonify
from flask_xmlrpcre.xmlrpcre import XMLRPCHandler, Fault
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

handler = XMLRPCHandler('api')
handler.connect(app, '/')


def database():
    conn = sqlite3.connect('password_manager.db', check_same_thread=False)
    try:
        conn.execute(
            """CREATE TABLE USERS(USERNAME TEXT, MAIL TEXT, PASSWORD TEXT)""")
    except:
        cursor = conn.execute("SELECT * from USERS")

    return conn


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


@cross_origin(supports_credentials=True)
def add_create(addorCreate, service, username, password):
    conn = database()
    update_or_not = functionCallAdd(
        addorCreate, service, username, password, load_key(), conn)
    conn.close()
    return jsonify({'returnvalue': str(update_or_not)})


@cross_origin(supports_credentials=True)
def others(function, service, username):
    conn = database()
    retValue = functionCallOthers(
        function, service, username, load_key(), conn)
    conn.close()
    return jsonify({'returnvalue': str(retValue)})


@cross_origin(supports_credentials=True)
def getUsernames(user):
    conn = database()
    retValue = getAll(user, load_key(), conn)
    conn.close()
    return jsonify({'returnvalue': retValue})


@cross_origin(supports_credentials=True)
def addUser(username, mail, password):
    conn = database()
    alreadyThere = createUser(username, mail, password, load_key(), conn)
    conn.close()
    return jsonify({'returnvalue': str(alreadyThere)})


@cross_origin(supports_credentials=True)
def userValidation(username, password):
    conn = database()
    flag = checkUser(username, password, load_key(), conn)
    conn.close()
    return jsonify({'returnvalue': str(flag)})


@cross_origin(supports_credentials=True)
def forgotPassword(username):
    conn = database()
    forgot(username, load_key(), conn)
    conn.close()


if __name__ == '__main__':
    handler.register_function(add_create, 'addCreate')
    handler.register_function(others, 'others')
    handler.register_function(getUsernames, 'get')
    handler.register_function(addUser, 'addUser')
    handler.register_function(userValidation, 'userValidation')
    handler.register_function(forgotPassword, 'forgotPassword')
    app.run(debug=True, host="localhost", port=5050)
