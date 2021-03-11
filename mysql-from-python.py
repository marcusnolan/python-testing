import os
import datetime
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('root')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        rows = cursor.execute("Delete from Friends where name = 'Bob';")
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    connection.close()