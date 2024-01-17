# p26globalfunc1
a = 10
b = 20
c = 30
d = 40
def operation():
    d = globals()
    print("--------------------------------------------")
    print("Out Function / Program Global variable Values")
    print("--------------------------------------------")
    print("\tValue a =",d["a"])
    print("\tValue b =", d.get("b"))
    print("\tValue c =", globals()["c"])
    print("\tValue d =", globals().get("d"))


operation()