def dispinfo(**a):
    print("="*50)
    print("Type of a =",type(a))
    print("No. of (key, value) = {}".format(len(a)))
    for k,v in a.items():
        print("\t{} ---> {}".format(k,v))
    else:
        print("="*50)


# main program
dispinfo(sno=10,sname="sdf",marks=33,cname="PSF")
dispinfo(eno=1,ename="DR",sal=4.5)
dispinfo(crs1="Java",crs2="Python")
dispinfo(author="Ritchie")
dispinfo()