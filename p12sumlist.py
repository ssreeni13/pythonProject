lst=[1,2,3,4,5,6]
s=0
i=0
print("-" * 40)
print("Elements of list:")
print("-"*40)
while(i<len(lst)):
    print("\t{}".format(lst[i]))
    s=s+lst[i]
    i=i+1
else:
    print("-" * 40)
    print("\tsum= {}".format(s))
    print("-" * 40)