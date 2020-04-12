import database_connection

@database_connection.connection_handler
def get_all(cursor):
    cursor.execute('''SELECT * FROM stream''')
    return cursor.fetchall()