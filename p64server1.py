import socket
s=socket.socket()
s.bind(("localhost",9000))
s.listen(3)
print("-------------------------------------------")
print("Server side program is Ready to accept client request...")
print("-------------------------------------------")
while True:
    con,addr=s.accept()
    cval=con.recv(1024).decode()
    print("Value from Client at Server side={}".format(cval))
    n=int(cval)
    res=n*n
    con.send(str(res).encode())