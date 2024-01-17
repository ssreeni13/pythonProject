print("Enter list of values separated by space:")
lst = [int(val) for val in input().split()]
print("Content of List:", lst)

print("===========OR==============")
ls = []
n = int(input("Enter how many values to be in list:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        val = int(input())
        ls.append(val)
    else:
        print("Content of list",ls)