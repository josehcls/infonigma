import sqlite3

conn = sqlite3.connect('db/nigma.db', check_same_thread=False)  

locks = dict([(1, slice(0,3)),(2, slice(3,9)), (3, slice(9,13)), (0, slice(0,13))])

def get_password(group):
    cursor = conn.cursor()
    cursor.execute('''SELECT resposta FROM nigma WHERE id = {0}'''.format(group))
    return cursor.fetchone()[0]

def get_lock_status (group, lock, passw):
    key = get_password(group)
    print(passw, key, key[locks[lock]])
    if passw == key[locks[lock]]:
        return True
    else:
        return False
