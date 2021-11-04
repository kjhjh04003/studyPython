# 데이터를 순차적으로 파악하는데 유용( 순서가 중요하지 않다면 셋을 이용)
# 리스트는 변경 가능하다.
# 리스트는 현재 위치에서 새로운 요소를 추가, 삭제하거나 기존 요소를 덮어쓸 수 있다.
# 동일한 값이 여러번 올 수 있다.

# 생성하기 : []
# 리스트는 0 혹은 그 이상의 요소로 만들어진다.
# ,로 구분하고 대괄호로 둘러싸여 있다.
empty_list = []
weekdays = ['Monday','Tuesday','Wednseday','Thursday','Friday']
big_birds = ['emu','ostrich','cassowary']
first_names = ['Graham','John','Terry','Terry','Michael'] # 중복 가능
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {'groundhog':'Phil'}, 'Feb.2']

# 생성 및 변환 : list()
# list() 함수로 빈 리스트를 만들 수 있다.
another_empty_list = list()
print(another_empty_list)
# list() 함수는 다른 데이터 타입을 리스트로 변환한다.
# 튜플을 리스트로 변환
print(list('cat'))
a_tuple = ('ready', 'fire','aim')
print(list(a_tuple))

# 문자열 분할로 생성 : split()
# 문자열을 구분자 단위로 분할하여 리스트 생성
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))
# 구분자가 두 개 이상일 때
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

# [offset]으로 항목 얻기
# 오프셋으로 특정 값 추출
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
# 음수 인덱스는 끝에서부터 거꾸로 출력
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# 슬라이스로 항목 얻기
# 슬라이스를 이용해서 리스트의 서브시퀀스를 추출할 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2]) # 리스트의 슬라이스도 리스트이다.
# 스텝 사용 가능
print(marxes[::2])
# 오른쪽에서 왼쪽으로 2칸씩 항목 추출
print(marxes[::-2])
# 리스트 반대로 뒤집기 - marxes리스트 자체는 변경되지 않음
print(marxes[::-1])
# list.reverse() : 리스트를 반대로 뒤집을 상태로 저장
marxes.reverse() # 리스트는 변경되지만 값을 반환하지 않는다.
print(marxes)
# 잘못된 인덱스로 접근하여도 예외 발생하지 않고 아무것도 반환하지 않는다.

# 리스트 끝에 항목 추가 : append()
# 리스트 끝에 새 항목을 한개씩 추가 -> 가변 객체이기 때문에
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

# 오프셋과 insert()로 항목 추가
# 원하는 위치에 항목 추가
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo') # 리스트의 끝을 넘는 오프셋에 입력하면 마지막에 저장된다.
print(marxes)

# 모든 항목 복제 : *
print(["blah"] * 3)

# 리스트 병합 : extend()와 +
# extend()를 사용해서 다른 리스트를 병합할 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
# + 나 += 로 병합할 수 있다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
# append()를 사용하면 항목을 병합하지 않고 others가 하나의 리스트로 추가된다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

# [offset]으로 항목 바꾸기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

# 슬라이스로 항목 바꾸기
numbers = [1,2,3,4]
numbers[1:3] = [8,9]
print(numbers)
# 리스트에 할당되는 오른쪽 값의 수는 왼쪽 슬라이스 항목 수와 달라도 된다.
numbers = [1,2,3,4]
numbers[1:3] = [7,8,9]
print(numbers)
numbers = [1,2,3,4]
numbers[1:3] = []
print(numbers)
# 오른쪽 값은 리스트가 아니여도 된다.
# 순회 가능한 타입 값을 리스트 항목에 할당할 수 있다.
numbers = [1,2,3,4]
numbers[1:3] = (98,99,100)
print(numbers)
numbers = [1,2,3,4]
numbers[1:3] = 'wat?'
print(numbers)

# 오프셋으로 항목 삭제 : del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
del marxes[-1]
print(marxes)
# 오프셋으로 리스트의 특정 항목을 삭제
# 이후 항목들은 한칸씩 앞당겨지고 리스트 길이도 감소
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)

# 값으로 항목 삭제 : remove()
# 삭제할 항목의 위치를 모른다면 remove()로 그 항목을 삭제
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)
# 리스트에 같은 값으로 항목이 중복이라면 remove()는 첫 번째 항목만 삭제한다.

# 오프셋으로 항목을 얻은 후 삭제 : pop()
# pop()은 리스트에서 항목을 가져오는 동시에 그 항목을 삭제한다.
# pop(0)은 리스트으 시작, pop() 또는 pop(-1)리스트의 마지막
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop()) # 해당 오프셋의 항목 반환
print(marxes)
print(marxes.pop(1))
print(marxes)

### append()로 새로운 항목을 끝에 추가한 뒤 pop()으로 다시 마지막 항목을 제거했다면, 후입선출(LIFO) 자료구조인 스택을 구현한 것이다.
### 그리고 pop(0)을 사용했다면 선입선출(FIFO) 자료구조인 큐를 구현한 것이다.
### 스택은 수집한 데이터에서 가장 오래된 것을 먼저 사용하는(FIFO)에 유용
### 큐는 수집한 데이터에서 최근 것을 먼저 사용하는 (LIFO)에 유용

# 모든 항목 삭제 : clear()
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

# 값으로 오프셋 찾기:index()
# 리스트 항목 값의 오프셋을 알고 싶을 때 사용
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))
# 리스트에 같은 값이 2개 이상일 때 첫번째 오프셋만 반환
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

# 존재 여부 확인 : in
# 리스트에 어떤 값의 존재를 확인할 때
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bart' in marxes)
# 리스트에 값이 적어도 하나 존재하면 in은 True 반환
words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)

# 값 세기 : count()
# 리스트에 특정 항목이 얼마나 있는지 세기 위함
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

# 문자열로 변환 : join()
# join()의 인수는 문자열 혹은 순회 가능한 문자열의 시퀀스다.
# 결과로 문자열을 반환한다.
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)

# 정렬하기 : sort()와 sorted()
# sort() : 리스트 자체를 내부적으로 정렬
# sorted() : 리스트의 정렬된 복사본을 반환
# 리스트의 항목이 숫자라면 오름차순(기본값)으로 정렬
# 문자열이면 알파벳순으로 정렬
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes) # marxes 정렬 후 복사본
print(marxes) # 원본 그대로
marxes.sort() # 원본 변경
print(marxes) # 원본 변경
# 혼합된 타입 정렬
numbers = [2,1,4.0,3]
numbers.sort()
print(numbers)
# 내림차순 정렬
numbers = [2,1,4.0,3]
numbers.sort(reverse=True)
print(numbers)

# 항목 개수 얻기 : len()
# 리스트의 항목수 반환
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

# 할당하기 : =
# 한 리스트를 변수 두 곳에 할당했을 때, 한 리스트를 변경하면 다른 리스트도 변경된다.
a = [1,2,3]
print(a)
b = a # 단지 a객체를 참조하는 것, a 또는 b를 변경하면 두 변수 모두에 반영
print(b)
a[0] = 'surprise'
print(a)
print(b)

# 복사하기 : copy(), list(), 슬라이스
# 한 리스트를 새로운 리스트로 복사할 수 있다.
# 이들은 자신만의 새로운 객체를 갖는다.
# 원본을 참조하지 않아 값을 변경하여도 영향을 주지 않는다.
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

# 깊은 복사 : deepcopy()
# 리스트 값이 모두 불면이면 copy() 메서드는 제대로 작동한다.
# 가변 객체는 참조일 뿐, 원본과 사본의 변경 사항을 모두 반영한다.
a = [1,2,[8,9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)
# 하위 리스트 변경
a[2][1] = 10 # 9를 10으로 변경
print(a)
print(b)
print(c)
print(d)

# 깊은 복사를 수행하는 deepcopy()
import copy
a = [1,2,[8,9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)

# 리스트 비교
# 비교연산자와 리스트를 직접 비교할 수 있다.
# 비교연산자는 두 리스트의 같은 위치의 오프셋 항목을 비교한다.
a = [7,2]
b = [7,2,9]
print(a==b)
print(a<=b)
print(a<b)
a = [3,2]
b=[1,2,3]
print(a>b)

# 순회하기:for과 in
cheeses = ['brie','gjetost','havarti']
for cheese in cheeses:
    print(cheese)
# break, continue 사용 가능
cheeses = ['brie','gjetost','havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
# break문 없이 완료되면 else 사용 가능
cheeses = ['brie','gjetost','havarti']
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'x'")
        break
    else:
        print(cheese)
else:
    print("Didn't find anything that started with 'x'")
# in 문의 리스트에 항목이 없어도 else가 실행
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

# 여러 시퀀스 순회 : zip()
# zip() 함수로 여러 시퀀스를 병렬로 순회 가능
days = ['Monday', 'Tuseday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
    print(day, ": drink", drink, "-eat", fruit, "-enjoy",dessert)
# 여러 시퀀스 중 짧은 시퀀스가 완료되면 zip()은 멈춘다.
# zip() 함수로 여러 시퀀스를 순회하며, 동일한 오프셋에 있는 항목부터 튜플을 만들 수 있다.
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english,french)))
print(dict(zip(english,french)))

# 리스트 컴프리헨션
# for/in 문의 순회 기능을 가진 리스트 컴프리헨션을 통해 리스트 생성 가능
number_list=[]
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
# 이터레이터와 range() 함수 사용
number_list = []
for number in range(1,6):
    number_list.append(number)
print(number_list)
# 리스트에 직접 range() 넣어서 결과 반환
number_list = list(range(1,6))
print(number_list)
# 리스트 컴프리헨션
# [표현식 for 항목 in 순회 가능한 객체]
number_list = [number for number in range(1,6)]
print(number_list)
number_list = [number-1 for number in range(1,6)]
print(number_list)
# 리스트 컴프리헨션은 조건 표현식을 포함할 수 있다.
# [표현식 for 항목 in 순회 가능한 객체 if 조건]
a_list = [number for number in range(1,6) if number%2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
    if number %2 == 1:
        a_list.append(number)
print(a_list)
# 리스크 컴프리헨션을 사용한 이중 루프
# 기존
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)
# 컴프리헨션 사용
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
# 언패킹 가능
for row, col in cells:
    print(row, col)

# 리스트의 리스트
small_bires = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_bires, extinct_birds, carol_birds]
print(all_birds)
# 첫번째 항목
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])