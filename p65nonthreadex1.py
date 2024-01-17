import time
def squares(lst):
    for n in lst:
        print("Square of {} = {}".format(n,n**2))
        time.sleep(1)

def cubes(lst):
    for n in lst:
        print("Cube of {} = {}".format(n,n**3))
        time.sleep(1)

bt=time.time()
lst=[10,20,30]
cubes(lst)
print("----------------------------")
squares(lst)
print("----------------------------")
et=time.time()
print("Total time taken by this non-threading programming=",(et-bt))
print("----------------------------")