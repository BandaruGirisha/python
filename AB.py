def pattern(n):
    for i in range(n):
        for j in range(65,65+n):
            print(chr(j),end='')
        print()
n=int(input('enter a no'))
pattern(n)
