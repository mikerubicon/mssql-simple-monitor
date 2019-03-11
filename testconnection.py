#!/usr/bin/env python 

##
# Monitor MSSQL server connection and data collation

import pyodbc
import os

def send_message(body, subject='Problem z połączeniem do bazy MSSQL',
recipient='user@email-domain.com'):
    os.system("echo '{}' |mail -s '{}' {}".format(body, subject, recipient))

# Connect to DSN defined in /etc/odbc.ini
# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Linux-or-Mac
DSN_STRING='DSN=XXXXXXXMSSQLServerName;UID=user;PWD=password'
try:
    connection = pyodbc.connect(DSN_STRING)
except pyodbc.Error as ex:
    sqlstate_code = ex.args[0]
    sqlstate_name = ex.args[1]
    message ='MSSQL {} - Connection ERROR! {} :: {}'.format(DSN_STRING,sqlstate_code,sqlstate_name)
    #print("Komunikat: {}".format(message))
    send_message(message)

cursor = connection.cursor()
cursor.execute("""SELECT some_ID AS id, some_NAME AS name
             FROM table
             ORDER BY some_NAME""")

rows = cursor.fetchall()
pltext = rows[XX][XX]
#print("Tekst z polskimi znakami ąśćł: {}".format(pltext))
teststring='ąśćł'

if teststring not in pltext:
    message='MSSQL {} - Data select ERROR! No test string.'.format(DSN_STRING)
    #print("Komunikat: {}".format(message))
    send_message(message)
