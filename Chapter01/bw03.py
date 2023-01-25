a = b'h\x65llo'
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # str 인스턴스

'''
str() vs repr()
str()
비공식적인 문자열을 출력
사용자가 보기 쉽도록
프로그램 사용자를 위해

repr
공식적인 문자열을 출력
문자열로 객체를 다시생성
프로그램 개발자를 위해서

참조: https://wikidocs.net/134994
'''
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8에서 한글은 3바이트임

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # bytes 인스턴스

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

'''
bytes와 str 두 종류가 존재
같은 인스턴스끼리만 더할 수 있다.
'''

'''
assert: 뒤의 조건이 True가 아니면 AssertError를 발생시킨다. 
assert 조건, '메세지' // 이와 같은 형태로 작성

lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]
def test(t):
    assert type(t) is int, '정수 아닌 값이 있네'

for i in lists:
    test(i)

>>>
Traceback (most recent call last):
  File "C:\Users\CVLab\PycharmProjects\test\EffectivePYTHON.py", line 61, in <module>
    test(i)
  File "C:\Users\CVLab\PycharmProjects\test\EffectivePYTHON.py", line 58, in test
    assert type(t) is int, '정수 아닌 값이 있네'
AssertionError: 정수 아닌 값이 있네

'''
