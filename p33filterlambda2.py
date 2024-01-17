print("Enter the list of values separated by space:")
lst = [int(val) for val in input().split()]
pslist = list(filter(lambda x:x>0,lst))
nglist = list(filter(lambda x:x<0,lst))
print("Original elements:",lst)
print("Positive elements:",pslist)
print("Negative elements:{}".format(nglist))