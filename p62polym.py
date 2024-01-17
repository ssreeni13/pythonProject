class Circle(object):
    def draw(self):  # original method
        print("Drawing Circle---Circle Class")

class Rect(Circle):
    def draw(self):  #overridden method
        super().draw()  #calling draw() of Circle class
        print("Drawing Rectangle---Rectangle Class")

class Square(Rect):
    def draw(self):    #overridden method
        super().draw()  #calling draw() of Rectangle class
        print("Drawing Square---Square Class")

so=Square()
so.draw()