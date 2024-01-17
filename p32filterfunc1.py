# This program takes list of values and extract +ve & -ve values
def pos(n):
    if n>0:
         return True
    else:
         return False

def neg(n):
    if n<0:
         return True
    else:
         return False


# main program
lst = [1,2,3,-45,90,67,-32,-54]
obj1 = filter(pos,lst)
pslist = list(obj1)
print("Type of obj1=",type(obj1))
print("Original elements:",lst)
print("Positive elements:",pslist)
obj2 = filter(neg,lst)
ngtpl = tuple(obj2)
print("Negative elements:{}".format(ngtpl))