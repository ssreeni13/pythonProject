import os
try:
    os.removedirs("e:\dir/df")
    print("Folder(s) Removed--Verify")
except FileNotFoundError:
    print("Specific Folder Hierarchy doesn't Exists")
except OSError:
    print("Specified Folder is not Empty")