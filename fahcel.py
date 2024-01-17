# ft=(9/5)*ct + 32 or ft=1.8*ct + 32
# kt=ct+273.15
type = input("Enter the Type Of Conversion you want..?(Fahrenheit/Kelvin) from Celsius ")
val = float(input("Enter the Value:"))

if type.lower() == "fahrenheit":
    ans = (9/5) * val + 32
    print(ans)
elif type.lower() == "kelvin":
    ans = val + 273.15
    print(ans)
else:
    print("Invalid input. Please choose either Fahrenheit or Kelvin.")


