# write a program which will compute sum of variable number of numerical values
def findsum(sname, *nums, city="Bangalore"):
    print("=" * 50)
    print("My Name is {} from {}".format(sname,city))
    print("Type of nums = ",type(nums))
    s = 0
    for val in nums:
        print("\t{}".format(val))
        s = s + val
    else:
        print("Sum = {}".format(s))
        print("="*50)


# main Program
findsum("Mahadev",1,2,3,4,5,city="Madurai")
findsum("Sreeni",10,3)
findsum("vasan",1,23,4,6)
findsum("nivas",1,20,3,40,5)