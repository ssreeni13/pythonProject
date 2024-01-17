# Write a python program which will accept 3 integer values and find the biggest

a= input("Enter 1st Value:")
b= input("Enter 2nd Value:")
c= input("Enter 3rd Value:")

big = a
if(a==b) or (b==c):
    print("All Values are Equal")
elif(b>big):
    big = b
    if(c>big):
        big = c
        print("Biggest = {}".format(big))
    else:
        print("Biggest = {}".format(big))
else:
    print("Biggest = {}".format(big))