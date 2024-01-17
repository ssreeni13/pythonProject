import threading
print("Name of Thread present in the Program",threading.currentThread().getName())
print("Enter a Number:")
a=int(input())
res=a*a
print("square({})={}".format(a,res))