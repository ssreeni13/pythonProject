bsfile = input("Enter Binary Source File:")
try:
    with open("bsfile","rb") as rp:
        bdfile = input("Enter Binary Destination File:")
        with open("bdfile", "w+b") as wp:
            sfdata = rp.read()
            wp.write(sfdata)
            print("{} data copied in to {} ---> Plz Verify".format(bsfile, bdfile))
except FileNotFoundError:
    print("Source File Doesn't Exists")

