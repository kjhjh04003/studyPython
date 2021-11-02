# boolean 타입 : True, False
# bool() : 모든 파이썬 데이터 타입을 boolean 타입으로 변환
#           어떤 값을 인수로 취해서 불리언 값을 반환

# 0이 아닌 값은 True
print(bool(True))
print(bool(1))
print(bool(45))
print(bool(-45))

# 0인 값은 False
print(bool(False))
print(bool(0))
print(bool(0.0))


# 정수 : 분수나 소수점이 없는 모든 수
# 정수에 쉼표를 사용할 수 없다.
print(1, 000, 000)  # 백만이라는 숫자 대신에 튜플을 얻는다.
# _를 사용하면 숫자로 구분할 수 있다.
print(1_2_3)

# 정수 연산자
# 덧셈, 뺄셈
print(5+9)
print(100-7)
print(4-10)
print(5+9+3)
print(4+3-2-1+6)
print(5+9   + 3)    # 숫자나 연산자 사이에 공백은 무시된다.

# 곱셈
print(6*7)
print(7*6)
print(6*7*2*3)

# 나눗셈
# / : 부동 소수점 포함
# // : 정수
print(9/5)
print(9//5)
# print(5/0)  # 0으로 나누면 예외
# divmod() : 소수점을 제외한 몫과 나머지를 동시에 구할 수 있다.
print(divmod(9,5))

# 거듭 제곱
print(2**3)
print(2.0**3)
print(0**3)


# 진수
# 정수 앞에 진수를 붙이지 않으면 10진수로 간주
# 2진수 : 0b 혹은 0B
# 8진수 : 0o 혹은 0O
# 16진수 : 0x 혹은 0X
print('10진수', 10)
print('2진수 10', 0b10)
print('8진수 10', 0o10)
print('16진수 10', 0x10)
value = 65
print('65를 2진수', bin(value))
print('65를 8진수', oct(value))
print('65를 16진수', hex(value))
# chr() : 정수를 단일 문자열로 변환
print(chr(65))
# ord() : 단일 문자열을 정수로 변환
print(ord('A'))

# 부동 소수점 : 소수점이 있는 숫자, float
# 부동소수점 숫자는 문자e와 정수인 지수를 포함할 수 있다.
print(5e0)
print(5e1)
print(5.0e1)
print(5.0*(10**1))
# 명확성을 위해 언더바를 사용해서 숫자를 구분할 수 있다.
million = 1_000_000.0
print(million)
print(1.0_0_1)


# 타입 변환
# int() : 정수 타입으로 변환
print(int(True))
print(int(False))
print(int(98.6))
print(int(1.0e4))
print(int('99'))
print(int(-23))
print(int('+12'))
print(type(int('1_000_000')))
print(int('10', 2)) # 2진수
print(int('10', 8)) # 8진수
print(int('10', 16)) # 16진수
print('10', 22) # 22진수
# bool() : 정수에 해당하는 boolean 값을 반환
print(bool(1))
print(bool(0))
print(bool(1.0))
print(bool(0.0))
# float() : 부동소수점 숫자로 타입 변환
print(float(True))
print(float(False))
print(float(98))
print(float('99'))
print(float('98.6'))
print(float('-1.5'))
print(float('1.0e4'))