import re
with open("dob.info","r") as rp:
    dobs=rp.read()
    dobslist=re.findall("\d{1,2}-\d{1,2}-\d{4}",dobs)
    print("-----------------------------------------")
    print("Data of Birth")
    print("-----------------------------------------")
    for db in dobslist:
        print("\t{}".format(db))
    print("-----------------------------------------")