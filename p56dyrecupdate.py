import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      cur = con.cursor()
      while True:
          try:
              print("----------------------------------------------")
              stno=int(input("Enter Student Number for Updating a Record:"))
              stmarks = float(input("Enter Student Marks for Updating a Record:"))
              sreeqry="update student set marks=%f where sno=%d"
              cur.execute(sreeqry %(stmarks,stno))
              con.commit()
              print("\n Number of Record Updated={}".format(cur.rowcount))
              print("----------------------------------------------")
              if cur.rowcount>=1:
                   print("Student Record Updated Successfully....")
              else:
                   print("Student Number and its Record Doesn't Exist")
              print("----------------------------------------------")
              ch=input("Do you want to Update another Record (yes/no):")
              if ch=="no":
                  break
          except ValueError:
              print("Don't Enter Strs / Special symbols / Alpha-Numeric Values")

except cx_Oracle.DatabaseError as db:
    print("Database Problem: ",db)
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")