# This function computes sum of two numbers by using function

# input ----> Taking from function call
# process ----> Inside of function body
# Result ----> inside of function body

# function heading with  formal variable
def addop(x,y):
    """This sum Program calls sum of two numbers"""
    # z is a local variable
    # process
    z = x + y
    # no return / output
    print("Sum({},{}) = {}".format(x,y,z))


# main program
a, b = int(input("Enter First Value:")), int(input("Enter Second Value:"))
# function call
addop(a,b)
print("Type of addop:",type(addop))
print("Doc String of addop:", addop.__doc__)