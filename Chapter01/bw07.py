# BETTER WAY 7 : range보다는 enumrate를 사용하라

l = ['a', 'b', 'c', 'd']

for i in l:
    print(i)

for i,j in enumerate(l):
    print(i, j)
    
'''
출력
a
b
c
d
0 a
1 b
2 c
3 d
'''
