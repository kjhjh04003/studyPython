# - 튜플은 불변 객체이다.
# - 튜플에 항목을 할당하고 나면 바꿀 수 없다.

# # 튜플 생성하기
# 1. 빈 튜플 만들기 : () 사용
# empty_tuple = ()
# 2. 한 요소 이상의 튜플을 만들기 위해서는 각 요소 뒤에 콤마(,)를 붙인다.
# -   요소 저장
one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',) #- 주의 사항 : 한 요소만 있고 콤마를 생략하면 튜플이 아니라 문자열이 된다.
print(one_marx)

# 2. 요소가 두 개 이상이면 마지막에는 콤마를 붙이지 않는다.
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

# 3. 튜플로 한 번에 여러 변수를 할당할 수 있다.
# - 이것을 튜플 언패킹이라고 한다.
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a,b,c = marx_tuple
print(a)
print(b)
print(c)

# # 튜플 생성하기 : tuple()
# - tuple() 함수는 다른 객체를 튜플로 만들어준다.
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

# 결합하기 : +
print(('Groucho',) + ('Chico','Harpo'))

# 복제하기 : *
print(('yada',)*3)

# 비교하기
a = (7,2)
b = (7,2,9)
print(a == b)
print(a <=b )
print(a < b)

# 순회하기 : for과 in
words = ('fresh','out','of','ideas')
for word in words:
    print(word)

# # 수정하기
# - 튜플은 문자열처럼 불변 객체이므로 기존 튜플을 변경할 수 없다.
# - 문자열과 같이 튜플을 결합하여 새 튜플을 만들 수 있다.
# - id() 함수를 이용하여 같은 객체인지 확인 가능하다.
t1 = ('Fee', 'Fie', 'Foe')
print(id(t1))
t2 = ('Flop',)
print(t1 + t2)
t1 += t2
print(t1)
print(id(t1))

# 튜플에는 컴프리헨션이 없다.
number_thing = (number for number in range(1,6))
print(number_thing)
print(type(number_thing)) # 제너레이터 객체를 반환