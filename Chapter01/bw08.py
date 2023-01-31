# BETTER WAY 8 : 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용하라

s = ['a', 'b', 'c', 'd']
t = ['가', '나', '다', '라']

for i, j in zip(s,t):
    print(i, j)
