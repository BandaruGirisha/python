a=int(input('enter a starting range'))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j)
        break
               
