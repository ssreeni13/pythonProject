import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", user="root", passwd="One1one$", database="sreenivasan")
    cur = con.cursor()
    sreeqry = "select * from student"
    cur.execute(sreeqry)
    print("-----------------------------------------")
    print("Student Records")
    print("-----------------------------------------")
    sree = cur.fetchall()
    # print(sree)
    for rec in sree:
        for val in rec:
            print("{}".format(val), end=" ")
        print("\n")
    print("-----------------------------------------")
except mysql.connector.DatabaseError as da:
    print("Problem in Getting Connection from Mysql DB",da)
# finally:
#     if con!=None:
#         con.close()
#         print("Db Connection Closed")