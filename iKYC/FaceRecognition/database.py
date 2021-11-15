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


def getCustomerID(conn, email):
    # '''
    # If login success, retrieve customerid for future queries
    # '''
    mycursor = conn.cursor()
    query = "SELECT customer_id FROM Customer WHERE email = '"+str(email)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()[0]

#######################################
# TRANSACTION PAGE #
#######################################


def getCustomerAccount(conn, customer_id):
    # '''
    # How to deal with specialization:
    # https://stackoverflow.com/questions/4361381/how-do-we-implement-an-is-a-relationship
    # '''
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT account_type, account_number, balance FROM Account WHERE customer_id = '" + \
        str(customer_id)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()
