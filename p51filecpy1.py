sfile=input("Enter the Source File:")
try:
    with open("sfile") as rp:
        dfile=input("Enter the Destination File:")
        with open("sfile","a") as wp:
            sfdata=rp.read()
            wp.write(sfdata)
            print("{} data copied in to {} ---> Plz Verify".format(sfile,dfile))
except FileNotFoundError:
    print("Source File Doesn't Exists")

