a = 10
b = 20
c = 30
d = 40
def operation():
    global c, d
    c = c + 1
    d = d + 1
    a = 1
    b = 2
    res = a + b + c + d + globals().get("a")+globals()["b"]
    print("Result",res)


operation()