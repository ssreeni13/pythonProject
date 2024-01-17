class Company:
    def getcompdet(self):
        self.cname = "Google"
        self.clocation= "Bangalore"

class Food:
    def getfooddet(self):
        self.avlfood="Egg Parotta"
        self.drink="Pomagrenate Juice"


class Employee(Company,Food):
    def getempdet(self):
        self.eno = 30
        self.ename = "Sreenivasan"
        self.sal = 99.50
        self.dsg= "Software Tester"

    def dispempdet(self):
        print("-----------------------------------------------")
        print("Employee Details")
        print("-----------------------------------------------")
        print("Employee Number:{}".format(self.eno))
        print("Employee Name:{}".format(self.ename))
        print("Employee Salary:{}".format(self.sal))
        print("Employee Designation:{}".format(self.dsg))
        print("Company Name:{}".format(self.cname))
        print("Company Location:{}".format(self.clocation))
        print("-----------------------------------------------")
        print("Food Details")
        print("-----------------------------------------------")
        print("Food in Company:{}".format(self.avlfood))
        print("Drink in Company:{}".format(self.drink))


#main Program
eo=Employee()
eo.getempdet()
eo.getcompdet()
eo.getfooddet()
eo.dispempdet()