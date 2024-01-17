from p46tcs import InValidNumberError
def multable():
    n = int(input("Enter a Number:"))
    if n<=0:
        raise InValidNumberError
    else:
        print("--------------------------------")
        print("Mul table of {}".format(n))
        print("--------------------------------")
        for i in range(1,13):
            print("\t{} x {}= {}".format(n,i,n*i))
        print("--------------------------------")
