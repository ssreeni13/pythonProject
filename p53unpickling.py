import pickle
try:
    with open("emp1.data","rb") as rp:
            print("-----------------------------------------------")
            print("Employee Records")
            print("-----------------------------------------------")
            while True:
                try:
                    emprec=pickle.load(rp)
                    # print("\t{}\t{}\t{}".format(emprec[0],emprec[1],emprec[2]))
                    for val in emprec:
                        print("{} ".format(val),end=" ")
                except EOFError:
                    print("\n-----------End of File------------------")
                    break
except FileNotFoundError:
    print("File doesn't Exists")