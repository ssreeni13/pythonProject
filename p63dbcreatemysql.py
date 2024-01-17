import mysql.connector
try:
      con = mysql.connector.connect(host="localhost",user="root",passwd="One1one$")
      print("Connection Obtained from MySql DB")
      print("------------------------------------")
      cur=con.cursor()
      # sreeqry="create table student(sno number(3),sname varchar2(10),marks number(5,2))"
      cur.execute("create database sreenivasan")
      print("Sreenivasan Database Created in MySql DB---Verify")
except mysql.connector.DatabaseError as db:
    print("Problem in Getting Connection from MySql DB:",db)




