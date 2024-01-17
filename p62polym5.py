class Circle:
    def area(self,r):
        ac=3.14*r*r
        print("Area of Circle:",ac)

class Square:
    def area(self,s):
        as1 = s * s
        print("Area of Square:",as1)
        print("---------------------------------------------------")
        # super().area(float(input("Enter Length of Rectangle:")),float(input("Enter Breadth of Rectangle:")))
        # print("--------------------------------------------------")
        # Circle.area(self,float(input("Enter Radius of Circle:")))

class Rect:
    def area(self,l,b=6):
        ar = l * b
        print("Area of Rectangle:", ar)

co=Circle()
so=Square()
ro=Rect()
lst=[]
lst.append(co)
lst.append(so)
lst.append(ro)
for obj in lst:
    obj.area(3)
print("--------------------------------------------------")
for obj in (co,so,ro):
    obj.area(6)
