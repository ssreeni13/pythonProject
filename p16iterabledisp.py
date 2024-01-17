# This program display the values of list, tuple, set, dictionary

def disp(k):
    print("Type of k =",type(k))
    print("-"*40)
    for val in k:
        print("\t{}".format(val),end=" ")
    else:
        print("\t-" * 40)


def dispdict(k):
    print("Type of k =",type(k))
    print("-"*40)
    for cno,cname in k.items():
        print("\t{} ----> {}".format(cno,cname))
    else:
        print("-" * 40)


# main program
lst = [10,20,30,40,50,60]
disp(lst)   # function call
tpl = ("Python", "Java", "Selenium", "api", "linux")
disp(tpl)   # function call
s = {2,"Virtualization",True,23.5}
disp(s)   # function call
d = {1:"Python", 2:"Data Science", 3:"Django",4:"Javascript"}
dispdict(d)  # function call
