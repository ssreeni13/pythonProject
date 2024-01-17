def posneg(lst):
    ps = []
    ng = []
    for val in lst:
        if val > 0:
            ps.append(val)
        else:
            ng.append(val)
    return ps, ng


print("Enter the list of values separated by space:")
lst1 = [int(val) for val in input().split()]
ps, ng = posneg(lst1)
print("Original elements:", lst1)
print("Positive elements:", ps)
print("Negative elements:{}".format(ng))
