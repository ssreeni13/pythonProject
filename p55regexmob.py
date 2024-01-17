import re
while True:
    mno=input("Enter Your Mobile Number:")
    if len(mno)==10:
        sres=re.search("\d{10}",mno)
        if sres != None:
            print("Your Mobile Number is Valid")
            break
        else:
            print("Your Mobile Number is not Valid,Bcoz it shouldn't contain str/special symbols")
    else:
        print("Mobile Number Must Contain 10 Digits")