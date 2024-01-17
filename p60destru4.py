import time
class Sample:
    def __init__(self):
        print("Object Initialization - Constructor")

    def __del__(self):
        print("Memory Space pointed by Object Removed--Garbage Collector")


#main program
lst= [Sample(),Sample(),Sample()]
print("We Created 3 Objects and Placed in lst")
time.sleep(5)
del lst
time.sleep(5)
print("End of Application")