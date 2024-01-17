# lang is global variable
lang = "Python"
def learnDataSci():
    crs1 = "Data Science"
    print("To do coding in {}, we need {} language".format(crs1,lang))
    # print(crs2,crs3) crs2 and crs3 can't access becoz they are local variable

def learnAI():
    crs2 = "AI"
    print("To do coding in {}, we need {} language".format(crs2,lang))
    # print(crs1,crs3) crs2 and crs3 can't access becoz they are local variable

def learnML():
    crs3 = "Machine Learning"
    print("To do coding in {}, we need {} language".format(crs3,lang))
    # print(crs1,crs2) crs2 and crs3 can't access becoz they are local variable

learnDataSci()
learnAI()
learnML()