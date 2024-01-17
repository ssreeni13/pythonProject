class Circle(object):
    def area(self,r):
        ac=3.14*r*r
        print("Area of Circle:",ac)

class Rect(Circle):
    def area(self,l,b):
        ar = l * b
        print("Area of Rectangle:", ar)

class Square(Rect):
    def area(self,s):
        as1 = s * s
        print("Area of Square:",as1)
        print("---------------------------------------------------")
        super().area(float(input("Enter Length of Rectangle:")),float(input("Enter Breadth of Rectangle:")))
        print("---------------------------------------------------")
        Circle.area(self,float(input("Enter Radius of Circle:")))

so=Square()
so.area(float(input("Enter Side of Square:")))