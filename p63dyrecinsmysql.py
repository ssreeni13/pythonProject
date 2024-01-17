import mysql.connector
try:
      con = mysql.connector.connect(host="localhost",user="root",passwd="One1one$",database="sreenivasan")
      cur = con.cursor()
      while True:
          try:
              print("----------------------------------------------")
              stno=int(input("Enter Student Number:"))
              stname = input("Enter Student Name:")
              # stmarks = float(input("Enter Student Marks:"))
              # colname = input("Enter College Name:")

              sreeqry="insert into student values(%d,'%s')"
              cur.execute(sreeqry %(stno,stname))
              con.commit()
              print("----------------------------------------------")
              print("Student Record Inserted Successfully....")
              print("----------------------------------------------")
              ch=input("Do you want to insert another Record (yes/no):")
              if ch=="no":
                  break
          except ValueError:
              print("Don't Enter Strs / Special symbols / Alpha-Numeric Values")

except mysql.connector.DatabaseError as db:
    print("Database Problem: ",db)
finally:
    if con!=None:
        con.close()
        print("Db Connection Closed")