# This program accept list of strings separated by comma and obtain single line
import functools
print("Enter the list of values separated by comma:")
lst = [str(val) for val in input().split(",")]

print("Content of List=",lst)
singleline = functools.reduce(lambda x,y:x+" "+y,lst)
print("Result={}".format(singleline))