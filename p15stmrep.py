# student marks report
while(True):
    while(True):
        sno= int(input("Enter the Student Number(1-200):"))
        if(sno>=1) and ((sno<=200)):
            break
    sname = input("Enter the Student Name:")

    while(True):
        cm = int(input("Enter the marks in C:"))
        if(cm>=1) and (cm<=100):
            break

    while(True):
        cppm = int(input("Enter the marks in C++:"))
        if(cppm>=1) and (cppm<=100):
            break

    while(True):
        pm = int(input("Enter the marks in Python:"))
        if(pm>=1) and (pm<=100):
            break

    totmarks = cm + cppm + pm
    percentage = (totmarks/300) * 100

    if((cm<40) or (cppm<40) or (pm<40)):
        grade = "FAIL"
    else:
        if((totmarks >= 250) and (totmarks <= 300)):
            grade = "DISTINCTION"
        elif ((totmarks >= 200) and (totmarks <= 249)):
            grade = "FIRST"
        elif ((totmarks >= 150) and (totmarks <= 199)):
            grade = "SECOND"
        elif ((totmarks >= 120) and (totmarks <= 149)):
            grade = "THIRD"

    print("="*50)
    print("\t\tStudent Progess Report")
    print("="*50)
    print("Student Number: {}".format(sno))
    print("Student Name: {}".format(sname))
    print("Student Marks in C: {}".format(cm))
    print("Student Marks in C++: {}".format(cppm))
    print("Student Marks in Python: {}".format(pm))
    print("="*50)
    print("Total Marks: {}".format(totmarks))
    print("Percentage Of Marks: {}".format(percentage))
    print("="*50)
    print("Student Result: {}".format(grade))
    print("="*50)
    print("Do you want to enter another Student Details(yes/no):")
    ch = input()
    if (ch == "no") or (ch == "NO") or (ch == "No"):
        print("Thanks for Using this Program..!")
        break