import time
class Sample:
    def __init__(self):
        print("Object Initialization - Constructor")

    def __del__(self):
        print("Memory Space pointed by Object Removed--Garbage Collector")


#main program
s1 = Sample()
s2 = Sample()
s3 = Sample()
print("We Created 3 Objects and Placed in lst")
time.sleep(5)
print("Object s1-Memory Space")
del s1 #gc is calling
time.sleep(5)
print("Object s2-Memory Space")
del s2
time.sleep(5)
print("Object s3-Memory Space")
del s3
time.sleep(5)
print("End of Application")