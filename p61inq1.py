class Univ:
    def getunivdet(self):
        self.uname=input("Enter Univ Name:")
        self.uloc=input("Enter Univ Location:")

    def dispunivdet(self):
        print("--------------------------------------------------")
        print("University Details")
        print("--------------------------------------------------")
        print("University Name:{}".format(self.uname))
        print("University Location:{}".format(self.uloc))
        print("--------------------------------------------------")


class College(Univ):
    def getcolldet(self):
        self.cname = input("Enter College Name:")
        self.cloc = input("Enter College Location:")
        self.getunivdet()

    def dispcolldet(self):
        self.dispunivdet()
        print("College Details")
        print("--------------------------------------------------")
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("--------------------------------------------------")

class Student(College):
    def getstuddet(self):
        self.sno = input("Enter Student Number:")
        self.sname = input("Enter Student Name:")
        self.crs = input("Enter Student Course:")
        self.getcolldet()
    def dispstuddet(self):
        self.dispcolldet()
        print("Student Details")
        print("--------------------------------------------------")
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Course:{}".format(self.crs))
        print("--------------------------------------------------")

#main program
so=Student()
so.getstuddet()
so.dispstuddet()
