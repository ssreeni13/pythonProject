import threading
print("Iam from python program")
t=threading.current_thread()
print("Type of t",type(t))
print("Name of thread",t.getName())
t.setName("Sree")
print("Name of thread=",t.getName())