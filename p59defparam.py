class Test:
    def __init__(self,a=10,b=20):
        self.a = a
        self.b = b
        print("Value of a = {}".format(self.a))
        print("Value of b = {}".format(self.b))


print("t1 Values")
t1 = Test()
print("t2 Values")
t2 = Test(2,3)
print("t3 Values")
t3 = Test(6)
print("t4 Values")
t4 = Test(b=50,a=30)
