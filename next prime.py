a=int(input('enter a starting range'))
j=a
while True:
    for i in range(2,j):
         if j%i==0:
            break
    else:
        print(j)
        break
    j+=1           
