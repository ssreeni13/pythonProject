import mysql.connector
try:
      con = mysql.connector.connect(host="localhost",user="root",passwd="One1one$",database="sreenivasan")
      cur = con.cursor()
      while True:
          try:
              print("----------------------------------------------")
              stno=int(input("Enter Student Number for Deleting a Record:"))
              # stname = input("Enter Student Name:")
              # stmarks = float(input("Enter Student Marks:"))
              # colname = input("Enter College Name:")

              sreeqry="delete from student where stno=%d"
              cur.execute(sreeqry %(stno))
              con.commit()
              print("----------------------------------------------")
              print("Student Record Deleted Successfully....")
              print("----------------------------------------------")
              ch=input("Do you want to delete another Record (yes/no):")
              if ch=="no":
                  break
          except ValueError:
              print("Don't Enter Strs / Special symbols / Alpha-Numeric Values")

except mysql.connector.DatabaseError as de:
    print("Database Problem: ",de)
# finally:
#     if con!=None:
#         con.close()
#         print("Db Connection Closed")