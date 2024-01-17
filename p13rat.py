# Right angle triangle pattern

n=int(input("How Many Star lines you want..? :"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
  for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()