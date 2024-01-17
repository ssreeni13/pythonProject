import re
try:
  fp=open("stud.info","r")
  fdata=fp.read()
  print("-----------------------------------------")
  print("Student Marks")
  print("-----------------------------------------")
  marklist = re.findall("\d{2}", fdata)
  for marks in marklist:
      print("\t{}".format(marks))
  print("-----------------------------------------")
  print("Student Names")
  print("-----------------------------------------")
  names = re.findall("[A-Z][a-z]+", fdata)
  for name in names:
      print("\t{}".format(name))
  print("-----------------------------------------")
except FileNotFoundError:
  print("File doesn't Exist")