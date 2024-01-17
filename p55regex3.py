import re
result=re.search("sreeni", "sreeni alse called as sreenivasan")

if result!=None:
    print("Search is Successful")
else:
    print("Search is not Successful")


# findall() ---->finding all matches and returns in the form of list
# findaiter() ---->finding all matches and returns in the form of <Callable_Iterator>object
# Search() ---->finding 1st match only and it never search further matches if we have
#          ---->if not matching it return None