import threading,time
def emp():
    print("Employee Started Working")
    print("Is Emp thread Alive...?=",threading.currentThread().is_alive())
    time.sleep(5)
    print("Employee Stopped Working")

# main program
print("Office Opened by Main Thread")
t1=threading.Thread(target=emp)
t1.start()
print("\nIs Main thread Alive...?=",threading.currentThread().is_alive())
t1.join()
print("Is Main thread Alive...?=",threading.currentThread().is_alive())
print("Is Child thread Alive...?=",t1.is_alive())
print("Office Closed")
