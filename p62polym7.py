class India:
    def capital(self):
        print("Delhi is the Capital of India")

    def lang(self):
        print("Hindi/Mix Lang Indian can Speak")

    def type(self):
        print("India is a Developing Country")


class USA:
    def capital(self):
        print("Washington is the Capital of USA")

    def lang(self):
        print("English Lang Americans can Speak")

    def type(self):
        print("USA is a Developed Country")


uo = USA()
ind = India()
print("-----------------------------------------")
for obj in [uo,ind]: # Here we are using object level polymorphism
    print("Ref of Obj=",type(obj))
    obj.capital()
    obj.lang()
    obj.type()
    print("-----------------------------------------")
