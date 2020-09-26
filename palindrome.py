n=int(input('enter a number'))
rev=0
a=n
while n>0:
    rem=n%10
    rev=rem+rev*10
    n=n//10
if a==rev:
    print(a,'is a palindrome number')
else:
    print(a,'is not a palindrome  number')
