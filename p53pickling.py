import pickle
with open("emp1.data","ab") as wp:
    noe = int(input("Enter How Many Employees Data You Have...?:"))
    for i in range(1,noe+1):
        print("-----------------------------------------------")
        print("Enter {} Employee Data:".format(i))
        print("-----------------------------------------------")
        eno=int(input("Enter Employee Number:"))
        ename = input("Enter Employee Name:")
        esal = float(input("Enter Employee Salary:"))
        lst=list()
        lst.append(eno)
        lst.append(ename)
        lst.append(esal)
        pickle.dump(lst,wp)
        print("-----------------------------------------------")
        print("{} Employee Data Record saved in a file Successfully:".format(i))
        print("-----------------------------------------------")