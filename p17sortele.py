# This program display the values of list, tuple, set, dictionary

def disp(k):
    print("Type of k =",type(k))
    print("-"*40)
    for val in k:
        print("\t{}".format(val),end=" ")
    else:
        print("\t-" * 40)


def sortelements(lst):
    print("Original Elements")
    disp(lst)
    lst.sort()
    print("Sorted Elements in Ascending Order")
    disp(lst)
    lst.reverse() # lst.sort(reverse=True)
    print("Sorted Elements in Descending Order")
    disp(lst)


# main program
# lst = [30,10,23,78,2,91]
print("Enter list of values separated by space:")
lst = [int(val) for val in input().split()]
sortelements(lst)   # function call