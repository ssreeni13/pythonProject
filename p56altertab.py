import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      print("Connection Obtained from Oracle DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="alter table student add(cname varchar2(10))"
      cur.execute(sreeqry)
      print("Student Table Altered in Oracle DB---Verify")
except cx_Oracle.DatabaseError as da:
    print("Problem in Getting Connection from Oracle DB")
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")