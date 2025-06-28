# def checkprime(no):
#     count = 0
#     for i in range(1,no+1,1):
#         if no%i==0:
#             count+=1
#     if count==2:
#             print("no is prime")
#     else:
#             print("no is not prime")
# checkprime(23)               


#prime num between 1 to 100

def primeno():
    for i in range (1,101,1):
        count=0
        for j in range(1,i+1,1):
            if i%j==0:
                count +=1
            if count ==2:
            #if i==j:
                print(i,end=" ")
primeno()                
