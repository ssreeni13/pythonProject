import re
with open("mail.info","r") as rp:
    maildata=rp.read()
    maillist=re.findall("\S+@\S+",maildata)
    print("------------------------------------------------")
    print("List of mails to contact")
    print("------------------------------------------------")
    for mlist in maillist:
        print(mlist)
    print("------------------------------------------------")