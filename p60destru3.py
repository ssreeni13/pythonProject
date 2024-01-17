import time
class Sample:
    def __init__(self):
        print("Object Initialization - Constructor")

    def __del__(self):
        print("Memory Space pointed by Object Removed--Garbage Collector")


#main program
s1 = Sample()
print("Object Created and Initialized")
s2=s1
s3=s2
print("Object s3 is Removed")
time.sleep(5)
print("Object s2 is Removed")
time.sleep(5)
print("Object s1 Memory Space is Going to Removed")
time.sleep(5)
print("End of Application")