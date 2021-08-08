#i=5
#while i<=25:
   # print(5,"*",5,"=",i)
  #  i=i+5
    #while
rows = 5
for i in range(5, rows + 5):
    for j in range(5, rows + 5):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
   