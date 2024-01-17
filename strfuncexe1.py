# String isX methods (str.isalnum(), str.isalpha(), str.isdigit(), etc.):
# Checking if a string satisfies specific conditions, such as being alphanumeric, alphabetic, or consisting of digits.

text = "12345"
is_alphanumeric = text.isalnum()  # True
is_alpha = text.isalpha()  # False
is_digit = text.isdigit()  # True
print(is_alphanumeric)
print(is_alpha)
print(is_digit)

# String Capitalization (str.title()): Capitalizing the first letter of each word in a string.

text = "python programming is fun"
capitalized = text.title()  # "Python Programming Is Fun"
print(capitalized)

