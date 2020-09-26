n=int(input('enter a number'))
s=0
a=n
while n>0:
    rem=n%10
    s+=rem
    n=n//10
if a%s==0:
     print(a,'is a harshed number')
else:
     print(a,'is not a harshed number') 
    
