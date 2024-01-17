# This function computes sum of two numbers by using function

# input ----> Taking inside from function call
# process ----> Inside of function body
# Result ----> inside of function body

# function heading with  formal variable
def addop():
    """This sum Program calls sum of two numbers"""
    # c is a local variable
    x = int(input("Enter First Value:"))
    y = int(input("Enter Second Value:"))
    # process
    z = x + y
    # no return / output
    print("Sum({},{}) = {}".format(x,y,z))

# main program
# function call
addop()

print("Type of addop:",type(addop))
print("Doc String of addop:", addop.__doc__)