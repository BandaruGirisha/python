def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
       return True
    else:
       return False 
def right_prime(n):
    i=n+1
    while 1:
        if is_prime(i):
            return i
        i+=1
def left_prime(n):
    j=n-1
    while 1:
        if is_prime(j):
            return j
        j-=1
def near_prime(n):
     if is_prime(n):
         print(n)
     else:
         x=right_prime(n)
         y=left_prime(n)
         if abs(n-x)<abs(n-y):
             print(x)
         elif abs(n-x)>abs(n-y):
             print(y)
         else:
             print(x,y)
n=10           
near_prime(n)             
