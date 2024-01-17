from p46tcs import InValidNumberError
from p46wipro import multable
try:
    multable()
except InValidNumberError:
    print("\nDon't Enter -ve/Zero Number")
except ValueError:
    print("\nDon't Enter Strs/Alpha Numeric/Special Symbols")
finally:
    print("Iam Finally Here....")