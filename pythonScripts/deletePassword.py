from .encryptPassword import *


def delete_password(service, username, user, conn, key):
    cursor = conn.execute("SELECT * from " + user)
    userkey = str(encrypt_message(''.join(hex(ord(x))[2:] for x in username), key)) + \
        str(encrypt_message(''.join(hex(ord(x))[2:] for x in service), key))
    for row in cursor:
        if bytes.fromhex(decrypt_message(bytes(row[0][2:-1], 'utf-8'), key)).decode('utf-8') == userkey:
            command = """DELETE FROM """ + str(encrypt_message(''.join(
                hex(ord(x))[2:] for x in user), key)) + """ WHERE USER_KEY = ?;"""
            values = (userkey, )
            conn.execute(command, values)
            conn.commit()
            break
