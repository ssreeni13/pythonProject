# program accepting two integer values and find biggest by using anonymous function
big = lambda a, b: a if a > b else b
small = lambda a, b: a if a < b else b


bv = big(float(input("Enter 1st value:")), float(input("Enter 2nd value:")))
print("Biggest = {}".format(bv))
sv = small(float(input("Enter 1st value:")), float(input("Enter 2nd value:")))
print("Smallest = {}".format(sv))
