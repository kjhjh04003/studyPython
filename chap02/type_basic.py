# type() : 어떤 타입의 변수 또는 리터럴 값을 알고 싶을 때
print(type(7))
print(type(7) == int)

# isinstance() : 변수가 특정 타입의 객체를 가리키는지 확인
print(isinstance(7, int))

# 여러 타입 확인
a = 7
b = a
print(type(a))
print(type(b))
print(type(58))
print(type(99.9))
print(type('abc'))

# 복사
# 불변 객체 복사
x = 5
y = x
print('x : ', x)
print('y: ', y)
x = 29
print('x : ', x)
print('y: ', y)

# 가변 객체 복사 : 불변 객체와 다르게 둘 중 하나를 통해 값이 변경되면 나머지도 똑같이 변경된다.
a = [2, 4, 6]
b = a
print('a : ', a)
print('b : ', b)
a[0] = 99
print('a : ', a)
print('b : ', b)