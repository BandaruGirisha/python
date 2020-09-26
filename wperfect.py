n=int(input('enter a number'))
s=0
i=1
while i<n:
    if n%i==0:
         s+=i
    i+=1     
if n==s:
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number') 
        
           
        
    
