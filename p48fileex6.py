try:
    with open("stud.data","r") as rp:
        print("File opened in read mode successfully")
        print("-----------------------------------------")
        print("File Opening Mode=", rp.mode) 
        print("is Readable ?=", rp.readable())
        print("is Writable ?=", rp.writable())
        print("line-->8, Is files Closed ?=", rp.closed)
        print("-----------------------------------------")
    print("Iam out of with open()... line-->10, Is files Closed ?=", rp.closed)
except FileNotFoundError:
    print("Files does not Exists")
else:
    print("Iam out of with open()... line-->14, Is files Closed ?=", rp.closed)
finally:
    print("Iam out of with open()... line-->16, Is files Closed ?=", rp.closed)