def rev_num(num):
    rev =0
    while num>0:
        rem = int(num%10)
        rev = (rev*10)+rem
        num = int(num/10)
        print()