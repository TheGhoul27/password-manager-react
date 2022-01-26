from .addPassword import *
from .deletePassword import *
from .updatePassword import *
from .mailPassword import *
from .getPassword import *
from .encryptPassword import *

'''import sqlite3


conn = sqlite3.connect('password_manager.db')

try:
    conn.execute(
        """CREATE TABLE USERS(USERNAME TEXT, MAIL TEXT, PASSWORD TEXT)""")

except:
    cursor = conn.execute("SELECT * from USERS")'''


def functionCallAdd(function, service, username, password, user, key, conn):
    user = 'P' + str(''.join(hex(ord(x))[2:] for x in user))
    if function == 'add':
        flag = add_password(username, service, password, user, conn, key)
    else:
        flag = add_password(username, service, 'u', user, conn, key)

    return flag


def functionCallOthers(function, service, username, password, user, key, conn):
    user = 'P' + str(''.join(hex(ord(x))[2:] for x in user))
    if function == 'update':
        update_password(service, username, password, user, conn, key)
    elif function == 'delete':
        delete_password(service, username, user, conn, key)
    else:
        return


def getAll(user, key, conn):
    user = 'P' + str(''.join(hex(ord(x))[2:] for x in user))
    return get_password(user, conn, key)


def forgot(user, key, conn):
    cursor = conn.execute("SELECT * from USERS")
    for row in cursor:
        userRetrive = bytes.fromhex(
            decrypt_message(row[0], key)).decode('utf-8')
        if userRetrive == user:
            mailid(bytes.fromhex(decrypt_message(row[2], key)).decode('utf-8'),
                   bytes.fromhex(decrypt_message(row[1], key)).decode('utf-8'))
            break


def createUser(user, mail, password, key, conn):
    if not checkUser(mail, password, key, conn):
        mail = 'P' + str(''.join(hex(ord(x))[2:] for x in mail))
        command = "CREATE TABLE " + \
            mail + " (USER_KEY TEXT, PASS_KEY TEXT)"
        conn.execute(command)
        command = "INSERT INTO USERS (USERNAME, MAIL, PASSWORD) VALUES (?, ?, ?)"
        user = encrypt_message(''.join(hex(ord(x))[2:] for x in user), key)
        mail = encrypt_message(''.join(hex(ord(x))[2:] for x in mail), key)
        password = encrypt_message(
            ''.join(hex(ord(x))[2:] for x in password), key)
        values = (user, mail, password)
        conn.execute(command, values)
        conn.commit()
        return True
    else:
        return False


def checkUser(user, password, key, conn):
    cursor = conn.execute("SELECT * from USERS")
    flag = False
    for row in cursor:
        userRetrive = bytes.fromhex(
            decrypt_message(row[1], key)).decode('utf-8')
        if bytes.fromhex(userRetrive[1:]).decode("utf-8") == user:
            if bytes.fromhex(decrypt_message(row[2], key)).decode('utf-8') == password:
                flag = True
            break

    return flag
