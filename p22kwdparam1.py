def disp(a,b,c,crs="Python"):
    print("{}\t{}\t{}\t".format(a,b,c,crs))

# main program
disp(1,2,3)
disp(a=11,b=2,c=24)
disp(b=11,a=2,c=24)
disp(c=11,b=2,a=24)
disp(crs="java",a=11,b=2,c=24)
# disp(c=11,2,24)   SyntaxError: positional argument follows keyword argument
# disp(11,2,crs="c",24)      SyntaxError: positional argument follows keyword argument
disp(11,2,c=24)
disp(11,b=2,c=24)
