try:
    rp=open("stud.data")
    print("Type of rp=",type(rp))
except FileNotFoundError:
    print("Files does not Exists")
else:
    print("File opened in read mode successfully")
    print("-----------------------------------------")
    print("File Opening Mode=",rp.mode)
    print("is Readable ?=",rp.readable())
    print("is Writable ?=",rp.writable())
    print("Is files Closed ?=",rp.closed)
    print("-----------------------------------------")
finally:
    if rp!=None:
        print("File Closed Successfully")
        rp.close()
        print("Is files Closed ?=",rp.closed)


