from threading import *
import time
class Sree(Thread):
    def run(self):
       for i in range(1,5):
           print("Iam from Child Thread")
           time.sleep(2)


# main program
s=Sree()
s.start()