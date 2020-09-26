n=int(input('enter a number'))
s=0
a=n
while n>0:
    rem=n%10
    s+=rem*rem*rem
    n=n//10
if a==s:
    print(a,'is a Armstrong number')
else:
    print(a,'is not a Armstrong number')
