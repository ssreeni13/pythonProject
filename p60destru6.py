import time
import sys
class Sample:
    def __init__(self):
        print("Object Initialization - Constructor")

    def __del__(self):
        print("Memory Space pointed by Object Removed--Garbage Collector")


#main program
s1 = Sample()
s2=s1
s3=s2
print("Ref of s1=",sys.getrefcount(s1))
print("End of Application")