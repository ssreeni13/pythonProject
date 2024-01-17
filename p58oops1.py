class Employee:
    @classmethod
    def appendcompname(cls):
        cls.compname="Wipro-HYD"

    def appendempvalues(self):
        print("Id in method=",id(self))
        print("--------------------------------------")
        self.empno=int(input("Enter Employee Number:"))
        self.empname = input("Enter Employee Name:")
        self.empsal = float(input("Enter Employee Salary:"))
        self.empdsg = input("Enter Employee Designation:")
        print("--------------------------------------")

    def dispempvalues(self):
            print("Id in method=", id(self))
            print("--------------------------------------")
            print("Employee Number: {}".format(self.empno))
            print("Employee Name: {}".format(self.empname))
            print("Employee Salary: {}".format(self.empsal))
            print("Employee Designation: {}".format(self.empdsg))
            print("Employee Company Name: {}".format(Employee.compname))
            print("--------------------------------------")

    @staticmethod
    def operation(a,b,ops):
        if ops=="+":
            print("{} {} {} = {}".format(a,ops,b,a+b))
        elif ops=="-":
            print("{} {} {} = {}".format(a,ops,b,a-b))
        elif ops=="*":
            print("{} {} {} = {}".format(a,ops,b,a*b))
        elif ops=="/":
            print("{} {} {} = {}".format(a,ops,b,a/b))
        elif ops=="//":
            print("{} {} {} = {}".format(a,ops,b,a//b))
        elif ops=="%":
            print("{} {} {} = {}".format(a,ops,b,a%b))
        elif ops=="**":
            print("{} {} {} = {}".format(a,ops,b,a**b))
        else:
            print("You Don't Know Arithmetic Operators---PLease Learn")

#main program
Employee.appendcompname()    # Calling explicitly we are calling method
eo1=Employee()  # when we create an object, it must initialized the object by calling one special method implicitly by PVM---- That special method is called Constructor
print("Id of eo1 in Main Program=",id(eo1))
eo1.appendempvalues()
eo2=Employee()
print("Id of eo1 in Main Program=",id(eo2))
eo2.appendempvalues()
print("===========================================")
eo1.dispempvalues()
eo2.dispempvalues()
print("==============================================================================")
print("Utility Operations")
print("==============================================================================")
eo1.operation(2,3,"*")
eo2.operation(2,3,"**")

