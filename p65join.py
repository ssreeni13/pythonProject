import threading,time
def emp():
    print("Employee Started Working")
    time.sleep(5)
    print("Employee Stopped Working")

print("Office Opened by Main Thread")
t1=threading.Thread(target=emp)
t1.start()
t1.join()
print("Office Closed")
