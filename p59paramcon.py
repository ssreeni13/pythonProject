class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b


t1 = Test(4,5)
print("Content of t1=", t1.__dict__)
t2 = Test(40,50)
print("Content of t2=", t2.__dict__)
t3 = Test(400,500)
print("Content of t1=", t3.__dict__)
