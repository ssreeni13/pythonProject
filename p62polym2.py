class Circle(object):
    def draw(self):  # original method
        print("Drawing Circle---Circle Class")

class Rect:
    def draw(self):  #overridden method
        print("Drawing Rectangle---Rectangle Class")

class Triangle:
    def draw(self):  #overridden method
        print("Drawing Triangle---Triangle Class")
class Square(Rect,Triangle,Circle):
    def draw(self):    #overridden method
        print("Drawing Square---Square Class")
        Circle.draw(self)
        Rect.draw(self)
        Triangle.draw(self)

so=Square()
so.draw()