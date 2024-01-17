import re
noc=0
matinfo=re.finditer("Sreeni","Sreeni is Good Boy")
print("-------------------------------------------")
for mat in matinfo:
    noc+=1
    print("Start Index: {}\t End Index: {}\t Value: {}".format(mat.start(),mat.end(),mat.group()))
else:
    print("-------------------------------------------")
    print("No of Occurences={}".format(noc))
    print("-------------------------------------------")

