import mysql.connector
from DEFINE import *


def connect():
    conn = mysql.connector.connect(
        host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
    return conn


def getLoginInfo(conn, email):
    # '''
    # password is in SHA1() hash-value
    # https://stackoverflow.com/questions/614476/storing-sha1-hash-values-in-mysql
    # '''
    mycursor = conn.cursor()
    query = 'SELECT password_ FROM Customer WHERE email = "' + str(email)+'"'
    print(query)
    mycursor.execute(query)
    return mycursor.fetchall()[0]
