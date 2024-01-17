import mysql.connector
try:
      con = mysql.connector.connect(host="localhost",user="root",passwd="One1one$",database="sreenivasan")
      print("Connection Obtained from MySql DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="insert into student values(30,'sreeni')"
      cur.execute(sreeqry)
      con.commit()
      print("Student Table Record Created in sreenivasan DB---Verify")
except mysql.connector.DatabaseError as db:
    print("Problem in Getting Connection from MySql DB:",db)




