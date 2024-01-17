# this program is accepts list of elements and gets its square root and square list
print("Enter the list of Old Salaries of Employees:")
oldsal = [int(val) for val in input().split()]
newsal= list(map(lambda sal:sal+sal*0.15, oldsal))

print("-"*50)
print("Old Salary\tNew Salary")
print("-"*50)
for old,new in zip(oldsal,newsal):
      print("\t{}\t{}".format(old,new))
print("-"*50)
