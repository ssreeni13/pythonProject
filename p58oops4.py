class Circle:
    @classmethod
    def setpi(cls):
        cls.pi=3.14
    def readradius(self,op):
        self.r=float(input("Enter Radius for {}:".format(op)))
        return self.r

class Bangalore:
    @staticmethod
    def operations(c):
        rad = c.readradius("Area")
        ac=3.14*rad*rad
        print("Area of Circle={}".format(ac))
        print("----------------------------------------")
        rad = c.readradius("Peri")
        pc=2*3.14*rad
        print("Perimeter of Circle={}".format(pc))
        print("----------------------------------------")

#main program
Circle.setpi()
co=Circle()
Bangalore.operations(co)
