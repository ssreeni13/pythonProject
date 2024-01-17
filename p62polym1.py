class Circle(object):
    def __init__(self):  #original constructor
        print("Drawing Circle---Circle Class")

class Rect(Circle):
    def __init__(self):  #overridden constructor
        super().__init__()  #calling __init__() of Circle class
        print("Drawing Rectangle---Rectangle Class")

class Square(Rect):
    def __init__(self):   #overridden constructor
        super().__init__()   #calling __init__() of Rectangle class
        print("Drawing Square---Square Class")

so=Square()
# so.draw()