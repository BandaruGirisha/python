a=int(input('enter a starting range'))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        bp=j
        print(j)
        break
               
k=a
while True:
    for i in range(2,k):
         if k%i==0:
            break
    else:
        ap=k
        print(k)
        break
    k+=1
if abs(a-ap)>abs(a-bp):
    print('nearest prime is',bp)
elif abs(a-ap)==abs(a-bp):
    print('nearest prime is',ap,bp)
else:
    print('nearest prime is',ap)

