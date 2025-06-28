no=int(input("enter the no:"))
for i in range(1,no+1,1):
    for j in range(no+1,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1,1):
        print("* ",end="  ")
    print()        
    
for i in range(no+1,0,-1):
    for j in range(no+1,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1,1):
        print("* ",end="  ")
    print()        