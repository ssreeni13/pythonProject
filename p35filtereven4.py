print("Enter the list of values separated by space:")
lst1 = [int(val) for val in input().split()]
evlst = tuple(filter(lambda n:n%2 == 0,lst1))
print("Original elements:", lst1)
print("Even elements:", evlst)