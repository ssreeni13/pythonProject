import random
rand=random.random()
randin=random.randint(1,10)
randran=random.randrange(10)
print(rand)
print(randin)
print(randran)


# float 0.1 to 2
lst=[10,20,30,40,50]
print(random.choice(lst))
print("-----------------------")
print("Original Elements={}".format(lst))
random.shuffle(lst)
print("Shuffled Elements={}".format(lst))
print("-----------------------")
strtpl=("P","Y","T","H","O","N")
print("Original Elements={}".format(strtpl))
random.shuffle(strtpl)
print("Shuffled Elements={}".format(strtpl))
print("-----------------------")
lstcrs=["Python","Java","C#","CPP","C","Js"]
print("Original Elements={}".format(lstcrs))
random.shuffle(lstcrs)
print("Shuffled Elements={}".format(lstcrs))
print("-----------------------")