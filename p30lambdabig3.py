big = lambda a,b,c:"All values are Equal" if(a==b) and (b==c) else a if(a>b) and (a>c) else b if(b>a) and (b>c) else c

print("Enter three values:")
bv = big(int(input()),int(input()),int(input()))
print("Biggest=",bv)