import sys

addop = lambda a, b: a + b
subop = lambda a, b: a - b
mulop = lambda a, b: a * b
divop = lambda a, b: a / b
floordivop = lambda a, b: a // b
modop = lambda a, b: a % b
expop = lambda a, b: a ** b

def aopmenu():
    print("=" * 50)
    print("Arithmetic Operations")
    print("=" * 50)
    print("\t1.Addition")
    print("\t2.Subtraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Floor Division")
    print("\t6.Modulo Division")
    print("\t7.Exponentiation")
    print("\t8.Exit")
    print("=" * 50)


# main program
def readvalues():
    x1 = float(input("Enter the first number: "))
    x2 = float(input("Enter the second number: "))
    return x1, x2

while True:
    aopmenu()
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        x1, x2 = readvalues()
        res = addop(x1, x2)
        print("Sum({},{}) = {}".format(x1, x2, res))
    elif ch == 2:
        x1, x2 = readvalues()
        res = subop(x1, x2)
        print("Difference({},{}) = {}".format(x1, x2, res))
    elif ch == 3:
        x1, x2 = readvalues()
        res = mulop(x1, x2)
        print("Product({},{}) = {}".format(x1, x2, res))
    elif ch == 4:
        x1, x2 = readvalues()
        res = divop(x1, x2)
        print("Division({},{}) = {}".format(x1, x2, res))
    elif ch == 5:
        x1, x2 = readvalues()
        res = floordivop(x1, x2)
        print("Floor Division({},{}) = {}".format(x1, x2, res))
    elif ch == 6:
        x1, x2 = readvalues()
        res = modop(x1, x2)
        print("Modulo Division({},{}) = {}".format(x1, x2, res))
    elif ch == 7:
        x1, x2 = readvalues()
        res = expop(x1, x2)
        print("Exponentiation({},{}) = {}".format(x1, x2, res))
    elif ch == 8:
        print("Thanks for Using this Program")
        sys.exit()
    else:
        print("Your Selection of Program is wrong!... Try Again")
