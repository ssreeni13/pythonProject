import socket
s=socket.socket()
s.bind(("localhost",8000))
s.listen(3)
print("-------------------------------------------")
print("Server side program is Ready to accept client request...")
print("-------------------------------------------")
while True:
    con,addr=s.accept()
    print("Type of con=",type(con))
    print("Type of addr=",type(addr))
    print("Server Program Connected to Client at {}".format(addr))
    print("-------------------------------------------")
    cdata=con.recv(1024).decode()
    print("Data from Client at Server side={}".format(cdata))
    print("-------------------------------------------")
    con.send("Hi,This is Sreenivasan from Server Side".encode())