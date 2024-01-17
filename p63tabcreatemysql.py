import mysql.connector
try:
      con = mysql.connector.connect(host="localhost",user="root",passwd="One1one$",database="sreenivasan")
      print("Connection Obtained from MySql DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="create table student(stno int primary key,name varchar(20) not null)"
      cur.execute(sreeqry)
      print("Student Table Created in sreenivasan DB---Verify")
except mysql.connector.DatabaseError as db:
    print("Problem in Getting Connection from MySql DB:",db)




