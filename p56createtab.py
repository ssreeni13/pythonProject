import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      print("Connection Obtained from Oracle DB")
      print("------------------------------------")
      cur=con.cursor()
      sreeqry="create table student(sno number(3),sname varchar2(10),marks number(5,2))"
      cur.execute(sreeqry)
      print("Student Table Created in Oracle DB---Verify")
except cx_Oracle.DatabaseError as da:
    print("Problem in Getting Connection from Oracle DB")
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")