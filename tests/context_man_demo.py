import contextlib
import sqlite3

# connect = sqlite3.connect('/home/formation/database.sqlite')
# try:
#     try:
#         cursor = connect.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS person (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             firstname VARCHAR,
#             lastname VARCHAR)""")
#         connect.commit()
#     except Exception:
#         connect.rollback()
#
#     try:
#         cursor.execute('INSERT INTO person(firstname, lastname) VALUES (?, ?)', ('Carlos', 'Gomez'))
#         connect.commit()
#     except Exception:
#         connect.rollback()
# finally:
#     connect.close()
#
#
# with sqlite3.connect('/home/formation/database.sqlite') as conn:
#     with conn.cursor() as cur:
#         cur.execute("""""")
#         conn.commit()
#
#     with conn.cursor() as cur:
#         cur.execute('INSERT INTO person(firstname, lastname) VALUES (?, ?)', ('Carlos', 'Gomez'))
#         conn.commit()


# @contextlib.contextmanager
# def transaction(conn):
#     try:
#         print("Open cursor")
#         cursor = conn.cursor()
#         yield cursor
#         print("Commit my transaction")
#         conn.commit()
#     except Exception:
#         print("I rollback my transaction")
#
# with sqlite3.connect('/home/formation/database.sqlite') as conn:
#     with transaction(conn) as cur:
#         cur.execute("""""")
#         cur.execute('INSERT INTO person(firstname, lastname) VALUES (?, ?)', ('Carlos', 'Gomez'))


@contextlib.contextmanager
def raises(ExceptionType):
    try:
        yield
        raise Exception('We wait an exception')
    except ExceptionType:
        pass


class Transaction:

    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()


with sqlite3.connect('/home/formation/database.sqlite') as conn:
    with Transaction(conn) as cur:
        cur.execute("""""")
        cur.execute('INSERT INTO person(firstname, lastname) VALUES (?, ?)', ('Carlos', 'Gomez'))
