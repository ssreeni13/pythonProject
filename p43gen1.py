def sreerange(lb,ub,stp):
    if lb<ub:
        while lb<ub:
            yield lb
            lb=lb+stp
        else:
            print("Condition False")


result = sreerange(1,5,2)
print("Type of Result = {}".format(type(result)))
for i in result:
    print(i)