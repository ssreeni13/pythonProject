# This program which will accept list of employees salaries b/w 1000 to any salary,give 15% hike give to whose get more than 5000
# and give 30% hike give to whose get more less than 5000
print("Enter the list of Old Salaries of Employees:")
originalsal = [int(val) for val in input().split()]

# sallessthan5000 = list(map(lambda sal:sal+sal*(15/100),list(filter(lambda sal:sal<=5000,originalsal))))
# salmorethan5000 = list(map(lambda sal:sal+sal*(15/100),list(filter(lambda sal:sal>5000,originalsal))))

sallessthan5000 = list(filter(lambda sal:sal<=5000,originalsal))
hikesallessthan5000 = list(map(lambda sal:sal+sal*(30/100),sallessthan5000))
salmorethan5000 = list(filter(lambda sal:sal>5000,originalsal))
hikesalmorethan5000 = list(map(lambda sal:sal+sal*(15/100),salmorethan5000))
print("="*50)
print("\tSal Less than 5000\t Hike Salaries")
print("="*50)
for sal,hikesal in zip(originalsal,hikesallessthan5000):
         print("\t\t{}\t\t{}".format(sal,hikesal))
print("="*50)
print("="*50)
print("\tSal More than 5000\t Hike Salaries")
print("="*50)
for sal,hikesal in zip(originalsal,hikesalmorethan5000):
         print("\t\t{}\t\t{}".format(sal,hikesal))
print("="*50)