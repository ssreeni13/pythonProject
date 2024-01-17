class Circle:
    @classmethod
    def setpi(cls):
        cls.pi=3.14
    def readradius(self):
        self.r=float(input("Enter Radius:"))
        return self.r

class Bangalore:
    @staticmethod
    def operations(c):
        rad = c.readradius()
        ac=3.14*rad*rad
        print("Area of Circle={}".format(ac))
        print("----------------------------------------")
        pc=2*3.14*rad
        print("Perimeter of Circle={}".format(pc))
        print("----------------------------------------")

#main program
Circle.setpi()
co=Circle()
Bangalore.operations(co)
