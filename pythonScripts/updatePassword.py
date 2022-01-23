from .encryptPassword import *


def update_password(service, username, password, user, conn, key):
    cursor = conn.execute("SELECT * from " + user)
    userkey = str(encrypt_message(''.join(hex(ord(x))[2:] for x in username)), key) + \
        str(encrypt_message(''.join(hex(ord(x))[2:] for x in service), key))
    for row in cursor:
        x = [str(i) for i in row[1].split('|')]
        if bytes.fromhex(decrypt_message(bytes(row[0][2:-1], 'utf-8'), key)).decode('utf-8') == userkey:
            x[2] = str(encrypt_message(''.join(hex(ord(x))[2:]
                                               for x in password), key))
            rownew = str(x[0] + "|" + x[1] + "|" + x[2])
            command = """UPDATE """ + user + """ SET PASS_KEY = ? WHERE USER_KEY = ?;"""
            values = (rownew, userkey)
            conn.execute(command, values)
            conn.commit()
            break
