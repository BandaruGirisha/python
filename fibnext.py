n=int(input('enter a  range'))
a=0
b=1
for i in range(3,n+1):
     c=a+b
     a=b
     b=c
     if b>=n:
        print(b)
        break
                                        
