# BETTER WAY 6 : 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라
'''
튜플 인덱스 사용불가
'''

a = (1, 2)
try:
    a[0] = 0
except TypeError as t:
    print(t)
print(a)

x,y = a
print(x)
print(y)
