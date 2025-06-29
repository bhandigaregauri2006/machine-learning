per = int(input("enter the no:"))
if per>=75 and per<=100:
    print("distiction")
elif per>=60 and per<=74:
    print("First class")
elif per>=50 and per<=59:
    print("second  class")
elif per>= 35 and per<=49:
    print("pass class")
elif per<34 :
    print("fail")
else:
    print("invalid per")
