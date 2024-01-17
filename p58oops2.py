class Circle:
    @classmethod
    def setpi(cls):
        cls.pi=3.14

    def circlearea(self):
        print("----------------------------------------")
        self.r=float(input("Enter Radius for Area of Circle:"))
        self.ac=Circle.pi*self.r*self.r
        print("Area of Circle={}".format(self.ac))
        print("----------------------------------------")

    def circleperi(self):
        print("----------------------------------------")
        self.r = float(input("Enter Radius for Perimeter of Circle:"))
        self.pc = 2 * self.pi * self.r
        print("Perimeter of Circle={}".format(self.pc))
        print("----------------------------------------")

#main program
Circle.setpi()
co=Circle()
co.circlearea()
co.circleperi()