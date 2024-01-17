from threading import *
import time
class Sree:
    def show(self):
       for i in range(1,5):
           print("Iam from Child Thread")
           time.sleep(2)


# main program
s=Sree()
t=Thread(target=s.show())
t.start()