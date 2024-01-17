import threading,time
def show():
    print("Iam from Started Execution")
    print("Name of Child thread=",threading.currentThread().getName())
    time.sleep(5)
    print("Iam from Ended Execution")

t1=threading.Thread(target=show)
t1.start()
print("Iam from Python Program")
print("Name of Main thread=",threading.currentThread().getName())
print("Number of Active thread=",threading.activeCount())
t1.join()
print("Number of Active thread=",threading.activeCount())
