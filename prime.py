a=int(input("enter the number"))
i=1
c=0
while i<=a:
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print("it is a prime number")
    
else:
    print(" it is not prime number")
    