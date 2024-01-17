from p47atmmenu import atmmenu
from p47bankexcept import DepositError
from p47bankexcept import WithDrawError
from p47bankexcept import InSuffFundError
from p47bank import deposit
from p47bank import withdraw
from p47bank import balenq

import sys
while True:
    try:
        atmmenu()
        ch = int(input("Enter Your Choice:"))
        if ch==1:
           try:
               deposit()
           except ValueError:
               print("Don't Try to Deposit Strs/Alpha Numeric/Specific Symbols")
           except DepositError:
               print("Don't Try to Deposit -ve and Zero amount")
        elif ch == 2:
            try:
                withdraw()
            except ValueError:
                print("Don't Try to Withdraw Strs/Alpha Numeric/Specific Symbols")
            except WithDrawError:
                print("Don't Try to Withdraw -ve and Zero amount")
            except InSuffFundError:
                print("You Don't have Sufficient Funds")
        elif ch == 3:
            balenq()
        elif ch == 4:
            print("Thanks for using this App...!")
            sys.exit()
        else:
            print("Your Choice of Operation is Wrong,Select Properly")
    except ValueError:
        print("Don't Enter Strs/Alpha Numeric/Special Symbols as Choice")