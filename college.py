from univ import Univ
class College(Univ):
    def getcolldet(self):
        self.cname = input("Enter College Name:")
        self.cloc = input("Enter College Location:")
        # self.getunivdet()

    def dispcolldet(self):
        # self.dispunivdet()
        print("College Details")
        print("--------------------------------------------------")
        print("College Name:{}".format(self.cname))
        print("College Location:{}".format(self.cloc))
        print("--------------------------------------------------")