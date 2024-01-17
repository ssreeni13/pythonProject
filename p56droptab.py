import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      print("Connection Obtained from Oracle DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="drop table student"
      cur.execute(sreeqry)
      print("Student Table Dropped in Oracle DB---Verify")
except cx_Oracle.DatabaseError as de:
    print(de)
    # print("Problem in Getting Connection from Oracle DB")
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")