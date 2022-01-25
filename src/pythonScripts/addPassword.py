from .createPassword import *
from .encryptPassword import *


def add_password(username, service, passw, user, conn, key):
    cursor = conn.execute("SELECT * from " + user)
    username = str(encrypt_message(
        ''.join(hex(ord(x))[2:] for x in username), key))
    service = str(encrypt_message(
        ''.join(hex(ord(x))[2:] for x in service), key))
    userkey = username + service
    val = 0
    for row in cursor:
        if row[0] == userkey:
            val = 1

    if val == 0:
        if passw == "u":
            passkey = str(create_password())

        else:
            passkey = passw
        passkey1 = str(encrypt_message(
            ''.join(hex(ord(x))[2:] for x in passkey), key))
        passkey1 = username + "|" + service + "|" + passkey1
        command = 'INSERT INTO ' + user + \
            ' (USER_KEY, PASS_KEY) VALUES (?, ?);'
        values = (userkey, passkey1)
        conn.execute(command, values)
        conn.commit()

    return val
