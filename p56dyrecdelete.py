import cx_Oracle
try:
      con = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
      cur = con.cursor()
      while True:
          try:
              print("----------------------------------------------")
              stno=int(input("Enter Student Number for deleting a Record:"))
              sreeqry="delete from student where sno=%d"
              cur.execute(sreeqry %stno)
              con.commit()
              print("----------------------------------------------")
              print("Student Record Deleted Successfully....")
              print("----------------------------------------------")
              ch=input("Do you want to Delete another Record (yes/no):")
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