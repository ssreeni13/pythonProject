import time
class Sample:
    def __init__(self):
        print("Object Initialization - Constructor")

    def __del__(self):
        print("Memory Space pointed by Object Removed--Garbage Collector")


#main program
s1 = Sample()
time.sleep(5)
s1=None
print("End of Application")