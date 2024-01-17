import cx_Oracle
try:
      sreecon = cx_Oracle.connect("SYSTEM/SYSTEM@localhost/orcl")
except cx_Oracle.DatabaseError as da:
    print("Problem in Getting Connection from Oracle DB")
else:
    print("Python Program obtains connection from Oracle Database--Successfully")
finally:
    if sreecon!=None:
        sreecon.close()
        print("Db Connection Closed")