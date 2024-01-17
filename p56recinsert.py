import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      print("Connection Obtained from Oracle DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="insert into student values(30,'MVR',40.50,'HCU')"
      cur.execute(sreeqry)
      con.commit()
      print("Student Record inserted in Student Table---Verify")
except cx_Oracle.DatabaseError as da:
    print("Problem in Getting Connection from Oracle DB")
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")