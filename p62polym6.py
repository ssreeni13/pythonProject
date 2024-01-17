class India:
    def capital(self):
        print("Delhi is the Capital of India")

    def lang(self):
        print("Hindi/Mix Lang Indian can Speak")

    def type(self):
        print("India is a Developing Country")


class USA(India):
    def capital(self):
        print("Washington is the Capital of USA")
        India.capital(self)
        print("-------------------------------------------")
    def lang(self):
        print("English Lang Americans can Speak")
        super().lang()
        print("-------------------------------------------")
    def type(self):
        print("USA is a Developed Country")
        super().type()
        print("-------------------------------------------")
        
uo=USA()
uo.capital()
uo.lang()
uo.type()