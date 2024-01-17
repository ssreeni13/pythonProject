# def dispvalues(a):
#         print("{}".format(a))
#
# def dispvalues(a,b):
#         print("{}\t{}".format(a,b))
#
# def dispvalues(a,b,c):
#         print("{}\t{}\t{}".format(a,b,c))

def dispvalues(*a):
    for val in a:
        print("{}".format(val),end=" ")
    else:
        print()

#main Pragram
print("="*50)
dispvalues(10)
dispvalues(10,20)
dispvalues(10,20,30)
dispvalues(10,20,30,40)
dispvalues("S","R","E","E","N","I")
print("="*50)