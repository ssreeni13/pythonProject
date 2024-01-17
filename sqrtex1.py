n=float(input("Enter a Number:"))
res=n**0.5
# or n**(1/2)
print("sqrt({}))={}".format(n,res))
print("--------OR-----------")
print("sqrt({}))={}".format(n,round(res,2)))
print("--------OR-----------")
print("sqrt(%f)=%0.2f" %(n,res))