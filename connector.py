import mysql.connector
from mysql.connector import connection

def dbconnect():
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwertyuiop",
    database="sensedata"
  )
  return connection