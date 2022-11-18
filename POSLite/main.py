import sqlite3

try:
    sqliteConnection = sqlite3.connect('IMPD.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)

    sql_query = """UPDATE settings SET value='true' WHERE id=4"""

    cursor.execute(sql_query)

    sqliteConnection.commit()
    print('Successfully Finished')    
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

