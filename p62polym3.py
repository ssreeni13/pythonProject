class Circle(object):
    def __init__(self):  # original method
        print("Drawing Circle---Circle Class")

class Rect:
    def __init__(self):  #overridden method
        print("Drawing Rectangle---Rectangle Class")

class Triangle:
    def __init__(self):  #overridden method
        print("Drawing Triangle---Triangle Class")
class Square(Rect,Triangle,Circle):
    def __init__(self):    #overridden method
        print("Drawing Square---Square Class")
        Circle.__init__(self)
        Rect.__init__(self)
        Triangle.__init__(self)

so=Square()
# so.draw()