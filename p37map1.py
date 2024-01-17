# this program is accepts list of elements and gets its square root and square list
print("Enter the list of values separated by space:")
oldlst = [int(val) for val in input().split()]
sqrtlst = tuple(map(lambda val:val**0.5, oldlst))
sqrlst = tuple(map(lambda val:val**2,oldlst))
print("-"*50)
print("Original\tSquareRoot\tSquare")
print("-"*50)
for on,sqrtno,sqrno in zip(oldlst,sqrtlst,sqrlst):
      print("\t{}\t{}\t\t{}".format(on,round(sqrtno,2),sqrno))
print("-"*50)

