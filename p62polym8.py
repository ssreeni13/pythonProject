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

class Country:
    @staticmethod
    def dispCountryinfo(obj):
        print("-----------------------------------------")
        print("Ref of Obj=", type(obj))
        obj.capital()
        obj.lang()
        obj.type()
        print("-----------------------------------------")




uo = USA()
ind = India()

# Country.dispCountryinfo(uo)
# Country.dispCountryinfo(ind)
for sreeobj in (ind,uo):
    Country.dispCountryinfo(sreeobj)
