
# i=(len(a))-1
# num=int(input("enter the input"))
# while i>=0:
#      print(a[i])
#       i=i-1


a=[8,7]
i=0
max=a[i]
min=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        i+=1
    print("max",max)
    print("min",min)
