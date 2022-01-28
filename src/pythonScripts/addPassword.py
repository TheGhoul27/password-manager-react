from .createPassword import *
from .encryptPassword import *


def add_password(username, url, service, passw, user, conn, key):
    cursor = conn.execute("SELECT * from " + user)
    url = str(encrypt_message(
        ''.join(hex(ord(x))[2:] for x in url), key))
    username = str(encrypt_message(
        ''.join(hex(ord(x))[2:] for x in username), key))
    service = str(encrypt_message(
        ''.join(hex(ord(x))[2:] for x in service), key))
    userkey = username + service + url
    val = False
    for row in cursor:
        if row[0] == userkey:
            val = True

    if False == 0:
        if passw == "u":
            passkey = str(create_password())

        else:
            passkey = passw
        passkey1 = str(encrypt_message(
            ''.join(hex(ord(x))[2:] for x in passkey), key))
        passkey1 = username + "|" + service + "|" + url + "|" + passkey1
        command = 'INSERT INTO ' + user + \
            ' (USER_KEY, PASS_KEY) VALUES (?, ?);'
        values = (userkey, passkey1)
        conn.execute(command, values)
        conn.commit()

    return val
