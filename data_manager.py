import database_connection

@database_connection.connection_handler
def get_personal_trainer(cursor):
    cursor.execute('''SELECT * FROM stream''')
    return cursor.fetchall()