try:
    wp=open("attend.data","x")
    print("Type of rp=",type(wp))
    print("File opened in read mode successfully")
    print("-----------------------------------------")
    print("File Opening Mode=",wp.mode)
    print("is Readable ?=",wp.readable())
    print("is Writable ?=",wp.writable())
    print("-----------------------------------------")
except FileExistsError:
    print("File already opened in write mode,we can't open again")
