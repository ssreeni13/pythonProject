big = lambda lst:max(lst)
small = lambda hyd:min(hyd)


print("Enter the list of values separated by space:")
lst = [int(val) for val in input().split()]

bv = big(lst)
sv = small(lst)

print("Biggest({}) = {}".format(lst,bv))
print("Smallest({}) = {}".format(lst,sv))