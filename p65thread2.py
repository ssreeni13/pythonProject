import threading
import time
def squares(lst):
    for n in lst:
        print("Square of {} = {}".format(n,n**2))
        time.sleep(1)

def cubes(lst):
    for n in lst:
        print("Cube of {} = {}".format(n,n**3))
        time.sleep(1)

# main program
bt=time.time()
lst=[10,20,30]
t1=threading.Thread(target=squares, args=(lst,))
t2=threading.Thread(target=cubes, args=(lst,))
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("Total time taken by thread based application=",(et-bt))
