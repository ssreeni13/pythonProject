class Account:
    def __init__(self):
        self.__acno=10
        self.cname="Sreenivasan"
        self.__bal=3.6
        self.__pin=4321
        self.bname="SBI"
    def __openPinCover(self):
        print("Your Pin is={}".format(self.__pin))