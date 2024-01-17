# This function computes sum of two numbers by using function

# input ----> Taking inside of function body
# process ----> Inside of function body
# Result ----> Gives in function call

# function heading with  formal variable
def addop():
    """This sum Program calls sum of two numbers"""
    # c is a local variable
    x = int(input("Enter First Value:"))
    y = int(input("Enter Second Value:"))
    # process
    z = x + y
    # here return statement used to return the result from the function
    return x,y,z


# main program
# function call

# result = addop()
# print("Sum({},{}) = {}".format(result[0],result[1],result[2]))

a,b,c = addop()
print("Sum({},{}) = {}".format(a,b,c))

print("Type of addop:",type(addop))
print("Doc String of addop:", addop.__doc__)
