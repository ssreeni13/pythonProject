# This function computes sum of two numbers by using function

# input ----> Taking from function call
# process ----> Inside of function body
# Result ----> Gives result in function call

# function heading with  formal variable
def addop(a,b):
    """This sum Program calls sum of two numbers"""
    # c is a local variable
    c = a + b
    # here return statement used to return the result from the function
    return c

# main program
# function call
x = int(input("Enter First Value:"))
y = int(input("Enter Second Value:"))
result = addop(x,y)
print("Sum=",result)
print("Type of addop:",type(addop))
print("Doc String of addop:", addop.__doc__)