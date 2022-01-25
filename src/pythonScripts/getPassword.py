from .encryptPassword import *


def get_password(user, conn, key):
    usernames = []
    cursor = conn.execute("SELECT * from " + user)
    for row in cursor:
        values = []
        x = [str(i) for i in row[1].split('|')]
        for i in x:
            values.append(bytes.fromhex(
                decrypt_message(bytes(i[2:-1], 'utf-8'), key)).decode('utf-8'))
        usernames.append(values)

    return usernames
