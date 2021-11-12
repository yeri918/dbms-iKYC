import mysql.connector
from DEFINE import *


def connect():
    conn = mysql.connector.connect(
        host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
    return conn
