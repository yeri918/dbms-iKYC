import mysql.connector
from DEFINE import *
from datetime import datetime


def connect():
    conn = mysql.connector.connect(
        host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
    return conn


def getLoginInfo(conn, email):
    mycursor = conn.cursor()
    query = 'SELECT password_ FROM Customer WHERE email="' + str(email)+'"'
    print(query)
    mycursor.execute(query)
    return mycursor.fetchall()[0]


def getCustomerID(conn, email):
    # '''
    # If login success, retrieve customerid for future queries
    # '''
    mycursor = conn.cursor()
    query = "SELECT customer_id FROM Customer WHERE email='"+str(email)+"'"
    print(query)
    mycursor.execute(query)

    return mycursor.fetchone()[0]


def updateLoginHistory(conn, customer_id):
    mycursor = conn.cursor()
    query = "INSERT INTO Login_ (customer_id, login_time) VALUES ('" + \
        str(customer_id)+"', NOW())"
    mycursor.execute(query)
    conn.commit()


def getCustomerAccount(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT account_type, account_number, balance FROM Account WHERE customer_id = '" + \
        str(customer_id)+"' LIMIT 5"
    mycursor.execute(query)
    return mycursor.fetchall()


def getTransactionHome(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT T.transaction_type, T.transaction_time, T.transaction_amount FROM Transaction_ T WHERE T.account_number IN (SELECT A.account_number FROM Account A WHERE customer_id = " + \
        str(customer_id)+") LIMIT 5;"
    mycursor.execute(query)
    return mycursor.fetchall()


def getLoginHistory(conn, customer_id):

    mycursor = conn.cursor(dictionary=True)
    query = "SELECT login_time FROM Login_ WHERE customer_id = '" + \
        str(customer_id)+"' AND login_id NOT IN (SELECT MIN(login_id) FROM Login_  WHERE customer_id = '" + \
        str(customer_id)+"') ORDER BY login_id DESC LIMIT 10"
    mycursor.execute(query)
    return mycursor.fetchall()

#######################################
# TRANSACTION PAGE #
######################################


def getCustomerName(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT first_name, last_name FROM Customer WHERE customer_id = '" + \
        str(customer_id)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()[0]

#######################################
# TRANSACTION PAGE #
######################################


def getCustomerAccountList(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT account_type FROM Account WHERE customer_id = '" + \
        str(customer_id)+"'"
    # print(query)
    mycursor.execute(query)
    return mycursor.fetchall()


def getTransactionHistory(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT T.transaction_type, T.account_number, T.transaction_time, T.transaction_amount, T.transaction_description FROM Transaction_ T WHERE T.account_number IN (SELECT A.account_number FROM Account A WHERE customer_id = " + \
        str(customer_id)+") LIMIT 10;"
    mycursor.execute(query)
    # print(query)
    return mycursor.fetchall()


def getmaxtransaction(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT MAX(T.transaction_amount) FROM Transaction_ T, Account A, Customer C WHERE T.account_number = A.account_number AND A.customer_id = C.customer_id AND T.transaction_type = 'transfer' AND C.customer_id = '"+str(customer_id)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()[0]['MAX(T.transaction_amount)']


def filterTransactionWithType(conn, account_number, time_from, time_to, amount_from, amount_to):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT transaction_type, account_number, transaction_time, transaction_amount, transaction_description FROM Transaction_ WHERE"
    if account_number != 'All':
        query += " account_number = '"+str(account_number)+"' AND "
    query += " transaction_time > '"+str(time_from)+"' AND transaction_time < '"+str(
        time_to) + "' AND transaction_amount > '"+str(amount_from)+"' AND transaction_amount < '"+str(amount_to) + "'"
    mycursor.execute(query)
    return mycursor.fetchall()

#######################################
# TRANSFER PAGE #
#######################################


def addTransactionSuccess(conn, account_number, transaction_amount, transaction_type, transaction_description):
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    if not transaction_description:
        # print("hi")
        transaction_description = "No remarks"
    try:
        mycursor = conn.cursor(dictionary=True)
        query = "INSERT INTO Transaction_ (account_number, transaction_time, transaction_amount, transaction_type, transaction_description) VALUES ('"+str(
            account_number)+"', NOW(), " + str(transaction_amount)+", '"+transaction_type+"', '"+transaction_description + "');"
        print(query)
        mycursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    try:
        query = "UPDATE Account SET balance = balance -" + \
            str(transaction_amount) + "WHERE account_number = '" + \
            str(account_number)+"'"
        mycursor.execute(query)
        conn.commit()
    except Exception as e:
        return False
    return True


def getAllAccountNumberOfCustomer(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT account_number, account_type FROM Account WHERE customer_id = '" + \
        str(customer_id)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()


def getRecentPayee(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT T2.to_account, C.first_name, C.last_name FROM (SELECT Tr.to_account FROM Transfer_ Tr, Transaction_ T, Account A, Customer C WHERE Tr.transaction_id = T.transaction_id AND T.account_number = A.account_number AND A.customer_id = C.customer_id AND T.transaction_type = 'transfer' AND C.customer_id = '"+str(
        customer_id)+"') T2, Customer C, Account A WHERE C.customer_id = A.customer_id AND A.account_number = T2.to_account "
    print(query)
    mycursor.execute(query)
    return mycursor.fetchall()

#######################################
# PROFILE PAGE #
#######################################


def getProfileInfo(conn, customer_id):
    mycursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM Customer WHERE customer_id = '"+str(customer_id)+"'"
    mycursor.execute(query)
    return mycursor.fetchall()[0]
