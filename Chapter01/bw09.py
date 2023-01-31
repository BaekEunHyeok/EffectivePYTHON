# BETTER WAY 9 : for나 while 루프 뒤에 else 블록을 사용하지 말라

'''
for나 while루프가 break로 끊나지 않으면 else 블록이 실행된다.
'''

for i in range(3):
    print(i)
else:
    print('--else--')

for i in range(3):
    if i == 2:
        break
    print(i)
else:
    print('--else--')

print('====================')


'''
출력
0
1
2
--else--
0
1
====================
'''
