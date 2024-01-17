# Write a python program which will accept any two values and interchange them without using third variable

a = input("Enter the first value:")
b = input("Enter the second value:")
print("-"*50)
print("Original value of a: {}".format(a))
print("Original value of b: {}".format(b))
a, b = b, a
print("-"*50)
print("Swapped value of a: {}".format(a))
print("Swapped value of a: {}".format(b))
print("-"*50)