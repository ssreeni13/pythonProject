from college import College
class Student(College):
    def getstuddet(self):
        self.sno = input("Enter Student Number:")
        self.sname = input("Enter Student Name:")
        self.crs = input("Enter Student Course:")
        self.getcolldet()
        self.getunivdet()
    def dispstuddet(self):
        self.dispunivdet()
        self.dispcolldet()
        print("Student Details")
        print("--------------------------------------------------")
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Course:{}".format(self.crs))
        print("--------------------------------------------------")