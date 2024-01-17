# Write a python program which will generate ONE to N numbers. Where n must be a positive integer value.
n = int(input("Enter the number:"))
if(n<=0):
    print("{} is an invalid output".format(n))
else:
    print("-"*40)
    print("Numbers with in: {}".format(n))
    print("-"*40)
    i = 1
    while(i<=n):
        print("\t{}".format(i))
        i=i+1
    print("-"*40)