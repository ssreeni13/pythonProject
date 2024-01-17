import threading,time
def show():
    print("Iam from Started Execution")
    ct=threading.currentThread()
    print("Name of Child thread=",ct.getName())
    ct.setName("student")
    print("Name of Child thread after changing=",ct.getName())

t1=threading.Thread(target=show)
t1.start()
mt=threading.currentThread()
print("Name of Main thread before changing=",mt.getName())
mt.setName("SREE")
print("Name of Child thread after changing=",mt.getName())
