import socket
s=socket.socket()
s.connect(("localhost",9000))
print("-------------------------------------------")
print("Client side program connected to Server side program...")
print("-------------------------------------------")
val=input("\nEnter a Message:")
s.send(val.encode())
sdata=s.recv(1024).decode()
print("-------------------------------------------")
print("Square of {} at Client Side:{}".format(val,sdata))
print("-------------------------------------------")
