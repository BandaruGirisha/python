n=int(input('enter a number'))
s=0
for i in range(1,n-1):
    if n%i==0:
      s+=i
if n==s:
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number') 
        
    
