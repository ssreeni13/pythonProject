import re
noc=0
matinfo=re.finditer("[^A-Za-z0-9]","Asv#4vg@aR59$Vw%8rP")
print("-------------------------------------------")
for mat in matinfo:
    noc+=1
    print("Start Index: {}\t Value: {}".format(mat.start(),mat.group()))
else:
    print("-------------------------------------------")


# Programmer-Defined Character Classes2
# =>Character Classes Prepared By Programmer according to search pattern which is used search in the Given Data.
# =>The complete Programmer-Defined Character Classes are given Below
# 1) [kvr]-->search for either k' or 'v' or 'r8
# 2) [^kvr]--->search for all except 'k' or 'v' or 'r'
# 3) [a-z]--->search for all small alphabets only10
# 4) [^a-z]-->search for all except small alphabets
# 5) [A-Z]--->search for all capital alphabets only
# 6) [^A-Z]--->search for all except capitalalphabetsnet
# 7) [0-9]----->search for all digits only14
# 8) [^0-9]----->search for all except digits only15
# 9) [A-Za-z ]--->search for capital and small alphabets only16
# 10) [^A-Za-z ]--->search for all except capital and small alphabets only
# 11) [A-Za-z0-9]-->search for capital and small alphabets and digits only(except specialsynmbols)
# 12) [^A-Za-z0-9]--->search for only special symbols
# ‐----------------
# Pre-Defined Character Classes in Regular Expression
# =>These classes are already defined in Regular expressions and they are used forpreparing different search patterns.
# =>Pre-Defined Character Classes in Regular Expression are given bellow.
# 1) \s ------>Search for space character only8
# 2) \S--.->Search for all except space character9
# 3) \d--->Search for digit only10
# 4) \D--->Search for all except digit11
# 5) \w---->Search for word character [A-Za-z0-9] (except special symbols)
# 6) \W--->Search for special symbols except word character [^A-Za-z0-9]
# 7) .------>search for all characters
# ----------------
# Quantifiers in Regular Expression
# => Quantifiers in Regular Expression is used for finding no of occurences of special symbol/alphabet/digit
# => They are
#     1) 'a' ------> Searching Exactly for "a"
#     2) 'a+' ------> Searching Exactly for either one "a" or more "a" s
#     3) 'a*' ------> Searching Exactly for either zero or one "a" or more "a" s
#
# note:
#     1)\dddddddddd  or  \d(10)
#     2)[A-za-z]+
#     3)\d{2}.d+