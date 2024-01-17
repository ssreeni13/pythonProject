import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      cur = con.cursor()
      sreeqry = "select * from student"
      cur.execute(sreeqry)
      print("-----------------------------------------")
      print("Student Records")
      print("-----------------------------------------")
      sree=cur.fetchmany(2)
      # print(sree)
      for rec in sree:
          for val in rec:
              print("{}".format(val),end=" ")
          print("\n")
      print("-----------------------------------------")
except cx_Oracle.DatabaseError as da:
    print("Problem in Getting Connection from Oracle DB")
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")