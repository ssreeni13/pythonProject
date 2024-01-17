print("Enter list of values separated by space:")
lst = [float(val) for val in input().split()]
print("Content of list",lst)
print("-"*40)
newlst = []
for val in lst:
    newlst.append(val*2)
else:
    print("Newlist:",newlst)

print("==================OR====================")
newlst1 = [val*2 for val in lst]
print("Newlist:",newlst1)
