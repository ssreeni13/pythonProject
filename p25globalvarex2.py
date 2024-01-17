a = 10
def increment():
    global a
    a = a + 1
    print("Val of a in func1() =",a)


def mulval():
    global a
    a = a * 2
    print("Val of a in func1() =",a)

print("Value of a in main program before increment=",a)
increment()
print("Value of a in main program after increment=",a)
mulval()
print("Value of a in main program after multiply=",a)