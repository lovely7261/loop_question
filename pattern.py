num=int(input("enter the number"))
i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ",end="")
        b=b+1
    j=1
    while(j<i):
        print(j,end="")
        j=j+1
    k=i
    while(k>0):
         print(k,end="")
         k=k-1
    print()
    i=i+1