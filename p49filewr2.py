wp = open("emp.data","w")
lst=[27,"Sreeni",234,"Bangalore"]
tpl=34,"vasan",678,"mangalore"
wp.writelines(str(lst)+"\n")
wp.writelines(str(tpl)+"\n")
s="Python\nis an \nOops Language"
wp.writelines(s)
print("Data written to the file-->Verify")