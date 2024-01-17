import functools
print("Enter the list of values separated by space:")
lst = [int(val) for val in input().split()]
big = functools.reduce(lambda x,y:x if x>y else y,lst)
small = functools.reduce(lambda x,y:x if x<y else y,lst)

print("\tList of Elements={}".format(lst))
print("\tBiggest Element={}".format(big))
print("\tSmallest Element={}".format(small))