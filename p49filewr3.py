with open("hyd.data","w") as wp:
    print("Enter Multiple lines of text(To Stop press stop):")
    while True:
        std=input()
        if std!="stop":
            wp.write(std+"\n")
        else:
            print("\nData written to the file successfully-->Verify")
            break
