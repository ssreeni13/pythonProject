import cirmod,sqmod,rectmod,sys
from menumod import menu

while True:
    menu()
    ch = int(input("Enter Your Choice:"))
    if ch == 1:
        cirmod.area()
    elif ch == 2:
        sqmod.area()
    elif ch == 3:
        rectmod.area()
    elif ch == 4:
        print("Thanks For Using this Program")
        sys.exit()
    else:
        print("Your Selection of Operation is Wrong, Kindly Try Again")
