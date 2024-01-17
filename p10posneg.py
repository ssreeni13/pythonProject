# Write a python program which will accept +ve number or -ve number and print 1,2,....n. And also print -1,-2,-3,....-n.

n = int(input("Enter the number:"))
if(n==0):
    print("{} is an invalid output".format(n))
else:
    print("-"*40)
    print("Numbers with in: {}".format(n))
    print("-"*40)
    i = 1
    while(i<=n):
        print("\t{}".format(i))
        i=i+1
    else:
        j=-1
        while(j>=n):
            print("\t{}".format(j))
            j = j - 1
        else:
            print("-"*40)