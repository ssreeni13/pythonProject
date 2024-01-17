# write a python program which will calculate simple interest and the total amount to pay

p = float(input("Enter the Simple Interest in (Amount):"))
t = float(input("Enter the Time in (Months):"))
r = float(input("Enter the Rate of Interest in (%):"))
si = (p*t*r)/100
amountpay = p + si
print("-"*50)
print("Results")
print("-"*50)
print("Principal Amount:",p)
print("Time:",t)
print("Interest:",r)
print("-"*50)
print("Simple Interest:",si)
print("Total Amount to Pay:",amountpay)
print("-"*50)