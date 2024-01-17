# Loop
# str1 = "89898327943ABC898997977"
# alphabets = ''
#
# for char in str1:
#     if char.isalpha():
#         alphabets += char
#
# print("Alphabets:", alphabets)

# list
# str1 = "89898327943ABC898997977"
# alphabets = ''.join([char for char in str1 if char.isalpha()])
#
# print("Alphabets:", alphabets)


# using filter
str1 = "89898327943ABC898997977"
alphabets = ''.join(filter(str.isalpha, str1))

print("Alphabets:", alphabets)




