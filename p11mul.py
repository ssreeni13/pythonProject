# Write a python program which will generate a multiplication table for a given number.

n = int(input("Enter the number:"))
if(n<=0):
    print("{} is an invalid output".format(n))
else:
    print("-"*40)
    print("Multiplication Table for: {}".format(n))
    print("-"*40)
    i = 1
    while(i<=12):
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("-"*40)