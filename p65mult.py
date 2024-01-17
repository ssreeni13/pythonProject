import threading,time
def multable():
    n = int(input("Enter a Number:"))
    if n<=0:
        print(n,"is Invalid Input")
    else:
        print("----------------------------------------")
        print("Multiplication Table of {}".format(n))
        print("----------------------------------------")
        for i in range(1,13):
            print("{} x {} = {}".format(n,i,n*i))
            time.sleep(0.5)
        print("----------------------------------------")

# main program
t1=threading.Thread(target=multable)
t1.start()