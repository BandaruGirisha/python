Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=['eswar','girisha','laxmi','giri','python','rupa','jyothi']
>>> name[1:6]
['girisha', 'laxmi', 'giri', 'python', 'rupa']
>>> name[-6:-1]
['girisha', 'laxmi', 'giri', 'python', 'rupa']
>>> name[5:1:-1]
['rupa', 'python', 'giri', 'laxmi']
>>> name[5:0:-1]
['rupa', 'python', 'giri', 'laxmi', 'girisha']
>>> name[-2:-7:-1]
['rupa', 'python', 'giri', 'laxmi', 'girisha']
>>> a=[3,5,8,4,7]
>>> a.append(9)
>>> a
[3, 5, 8, 4, 7, 9]
>>> a.insert(1,2)
>>> a
[3, 2, 5, 8, 4, 7, 9]
>>> a[2]=10
>>> a
[3, 2, 10, 8, 4, 7, 9]
>>> b=[5,6]
>>> a.append(b)
>>> a
[3, 2, 10, 8, 4, 7, 9, [5, 6]]
>>> len(a)
8
>>> a
[3, 2, 10, 8, 4, 7, 9, [5, 6]]
>>> a.extend(b)
>>> a
[3, 2, 10, 8, 4, 7, 9, [5, 6], 5, 6]
>>> a.pop()
6
>>> a
[3, 2, 10, 8, 4, 7, 9, [5, 6], 5]
>>> del a[4]
>>> a
[3, 2, 10, 8, 7, 9, [5, 6], 5]
>>> a.remove([5,6])
>>> a
[3, 2, 10, 8, 7, 9, 5]
>>> del a[2:4]
>>> a
[3, 2, 7, 9, 5]
>>> del a[0: ]
>>> a
[]
>>> a=[1,2,3,4,8,9,5]
>>> a.clear()
>>> a
[]
>>> a=[11,5,3,9,7,0]
>>> b=a
>>> b
[11, 5, 3, 9, 7, 0]
>>> a.pop()
0
>>> a
[11, 5, 3, 9, 7]
>>> b
[11, 5, 3, 9, 7]
>>> b=a.copy()
>>> a
[11, 5, 3, 9, 7]
>>> b
[11, 5, 3, 9, 7]
>>> a.pop()
7
>>> a
[11, 5, 3, 9]
>>> b
[11, 5, 3, 9, 7]
>>> a=[1,2,3]
>>> a*2
[1, 2, 3, 1, 2, 3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> 