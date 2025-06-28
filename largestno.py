no1 = int(input("enter the no:"))
no2 = int(input("enter the no:"))
no3 = int(input("enter the no:"))
if no1>no2 and no1> no3:
    print("maximum no1")
elif no2>no1 and no2>no3:
    print("maximum no2")
elif no3>no1 and no3>no2:
    print("maximum no3")
else:
    print("all same")
    