print("Enter the list of elements of 1st list:")
lst1 = [int(val) for val in input().split()]
print("Enter the list of elements of 2nd list:")
lst2 = [int(val) for val in input().split()]

sumlst = list(map(lambda x,y:x+y,lst1,lst2))

print("-"*50)
print("\tList1\tList2\tList1+List2")
print("-"*50)

for one,two,sum in zip(lst1,lst2,sumlst):
    print("\t{}\t{}\t{}".format(one,two,sum))
print("-"*50)