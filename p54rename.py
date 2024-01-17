import os
try:
    os.rename("e:\dir1","e:\yes")
    print("Folder(s) Renamed--Verify")
except FileNotFoundError:
    print("OLder Folder doesn't Exists")