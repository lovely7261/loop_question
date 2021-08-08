i=int(input("enter the number"))
a=i
b=0
while (i>0):
    b=b+(i%10)*(i%10)*(i%10)
    i=i//10
    if a==sum:
        print("its amstrong number")
    else:
        print("its not amstorong number")