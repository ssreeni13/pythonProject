import os
sree=os.walk(".")
for s,r,e in sree:
    print("Folder path={}".format(s))
    print("Sub Folder path={}".format(r))
    print("Files={}".format(e))