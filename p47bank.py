from p47bankexcept import DepositError
from p47bankexcept import InSuffFundError
from p47bankexcept import WithDrawError
acbal=500.00
def deposit():
    damt = float(input("Enter the Amount to Deposit:"))
    if damt<=0:
        raise DepositError
    else:
        global acbal
        acbal=acbal+damt
        print("You have Deposited: {}".format(damt))
        print("Available Balance after Deposit: {}".format(acbal))

def withdraw():
    wamt = float(input("Enter the Amount for Withdrawal:"))
    if wamt<=0:
        raise WithDrawError
    else:
        global acbal
        if acbal<wamt:
            raise InSuffFundError
        else:
            acbal=acbal-wamt
            print("Take the Cash and Enjoy...!")
            print("Available Balance after withdraw: {}".format(acbal))



def balenq():
    print("Your Available Balance: {}".format(acbal))