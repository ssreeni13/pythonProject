class Test:
    def __init__(self):
        self.a=10
        self.b=20
        

t1=Test()
print("Content of t1=",t1.__dict__)
t2=Test()
print("Content of t2=",t2.__dict__)
t3=Test()
print("Content of t1=",t3.__dict__)
