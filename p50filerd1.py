rp = open("hyd.data","r")
fdata=rp.read(3)
print(fdata)
print("--------------------------")
print("Pos of rp=",rp.tell())
fdata=rp.read(3)
print(fdata)
print("Pos of rp=",rp.tell())
rp.seek(0)
print("After seek Pos of rp=",rp.tell())