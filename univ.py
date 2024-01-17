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