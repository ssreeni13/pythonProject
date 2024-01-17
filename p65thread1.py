import threading
import  time
def hello():
    for i in range(6):
        print("Child Thread1---->Iam from Hello()")
        time.sleep(1)

def hi(ms):
    for j in range(6):
        print(ms,"----Iam Hi()")

# main Program
t1=threading.Thread(target=hello)
t2=threading.Thread(target=hi, args=("Child Thread2",))
t1.start()
t2.start()
for i in range(6):
    print("Main Thread---->Iam from disp()")
    time.sleep(1)