rp = open("hyd.data","r")
fdata=rp.readlines()
for line in fdata:
    print(line,end="")
    