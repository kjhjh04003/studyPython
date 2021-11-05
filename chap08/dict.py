# 딕셔너리
# 순서 x, 인덱스x
# 키 : 값 형태
# 키 값은 불변하는 파이썬의 어떤 타입이 와도 된다.
# 가변 객체로 키:값 요소를 추가, 삭제, 수정할 수 있다.

# 생성하기 : {}
# 키:값 쌍을 콤마로 구분
empty_dict={}
print(empty_dict)

bierce = {
    "day":"A period of twenty-four hours, mostly misspent",
    "positive":"Mistaken at the top of one's voice",
    "misfortune":"The kind of fortune that never misses"
}
print(bierce)

# 생성하기 : dict()
# 일반적방법
acme_customer = {'first':'Wile','middle':'E','last':'Coyote'}
print(acme_customer)
# dict() 사용
acme_customer = dict(first="Wile", middle="E", last="Coyote") # 인수의 이름이 공백과 예약어가 아니여야 한다.
print(acme_customer)

# 변환하기 : dict()
# dict() 함수를 사용해서 두 값으로 이루어진 시퀀스를 딕셔너리로 변환할 수 있다.
# 각 시퀀스의 첫번째 항목은 키로, 두번째 항목은 값으로 사용
lol = [['a','b'], ['c','d'], ['e','f']]
print(lol)
print(dict(lol))
lol = [('a','b'),('c','d'),('e','f')]
print(dict(lol))
tol = (['a','b'],['c','d'],['e','f'])
print(dict(tol))
los = ['ab','cd','ef']
print(dict(los))

# 항목 추가/변경 : [key]
# 딕셔너리는 키에 참조되는 항목에 값을 할당하면 된다.
# 딕셔너리에 이미 존재하는 키라면 그 값은 새 값으로 대체된다.
# 키가 존재하지 않는다면 새 값과 키가 사전에 추가된다.
pythons = {
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle' : 'Eric',
    'Jones' : 'Terry',
    'Palin' : 'Michael'
}
print(pythons)
# 추가
pythons['Gilliam'] = 'Gerry'
print(pythons)
# 수정
pythons['Gilliam'] = 'Terry'
print(pythons)
# 딕셔너리의 키는 반드시 고유해야 한다.
some_pythons={ # 동일한 키를 가진 값이 2개 있다.
    'Gilliam': 'Chapman',
    'John' : 'Cleese',
    'Eric' : 'Idle',
    'Terry' : 'Gilliam',
    'Michael' : 'Palin',
    'Terry' : 'Jones'
}
print(some_pythons) # 동일한 키로 값을 넣은다면 마지막에 넣은 값으로 변경된다.

# 항목 얻기 : [key]와 get()
# 딕셔너리에 키를 지정하여 상응하는 값을 얻는다.
print(some_pythons['John'])
# 키가 없다면 예외 발생
# print(some_pythons['Groucho'])
# 키존재 여부 확인 : in
print('Groucho' in some_pythons)
# 키존재 여부 확인 : get()
print(some_pythons.get('John'))
print(some_pythons.get('Groucho','Not a Python')) # 뒤의 옵션은 키가 존재 하지 않을 때 출력할 문구, 지정하지 않으면 None로 출력

# 모든 키 얻기 : keys()
# 딕셔너리의 모든 키 가져오기
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
print(signals.keys()) # type : dict_keys()
# keys()로 받은 dict_keys()타입의 데이터를 list로 만들고 싶을 때
print(list(signals.keys()))

# 모든 값 얻기 : values()
# 딕셔너리의 모든 값 가져오기
print(signals.values()) # dict_values 타입
# dict_values타입을 리스트로 변경
print(list(signals.values()))

# 모든 키-값 얻기 : itmes()
# 딕셔너리의 모든 키-값 얻기
print(signals.items()) # dict_items 타입
# dict_items타입을 리스트로 변경
print(list(signals.items())) # 각 키와 값은 튜플로 구성

# 길이 얻기 : len()
# 딕셔너리의 키-값 쌍의 갯수
print(len(signals))

# 결합하기 : {**a, **b}
# **를 사용하여 딕셔너리를 결합할 수 있다.
# 해당 방법으로 얕은 복사를 할 수 있다.
first = {'a':'agony', 'b':'bliss'}
second = {'b':'bagels', 'c':'candy'}
print({**first, **second})
# 딕셔너리를 두개 이상 결합할 수 있다.
third = {'d':'donuts'}
news = {**first, **third, **second}
print(news)
first['a'] = 'apple'
print(first)
print(news)

# 결합하기 : update()
# 한 딕셔너리의 키와 값들을 복사해서 다른딕셔너리에 붙여준다.
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Gilliam':'Terry',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
}
print(pythons)
other = {
    'Marx':'Groucho', 'Howard':'Moe'
}
pythons.update(other)
print(pythons)
# 두번째 딕셔너리를 첫번째 딕셔너리에 병합하려할 때, 두 딕셔너리에 같은 키:값이 있다면
# 두번째 딕셔너리 값으로 병합된다.
first = {'a':1,'b':2}
second = {'b':'platypus'}
first.update(second)
print(first)

# 키와 del로 항목 삭제
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

# 키로 항목 가져온 뒤 삭제 : pop()
# pop()은 get()과 del을 함께 사용
# 딕셔너리에 있는 키와 pop()의 인수가 일치한다면 해당 값을 반환한 뒤, 해당 키-값을 삭제, 일치하지 않으면 예외발생
print(len(pythons))
print(pythons.pop('Palin'))
print(len(pythons))
# print(pythons.pop('Palin')) # 키값이 존재하지 않으면 예외 발생
# pop()에 두번째 인수를 지정하면, get()과 같이 동작(키가 존재하지 않는다면 두번재 인수가 출력)
print(pythons.pop('Palin','Hugo'))
print(len(pythons))

# 모든 항목 삭제 : clear()
# 딕셔너리에 있는 키와 값 모두 삭제
pythons.clear()
print(pythons)

# 키 존재여부 확인 : in
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Jones':'Terry',
    'Palin':'Michael',
    'Idle':'Eric',
}
print('Chapman'in pythons)
print('Palin'in pythons)
print('Gilliam'in pythons)

# 할당하기 : = -> 원본 객체를 참조하는 것
# 딕셔너리를 할당한 후 변경할 때 딕셔너리를 참조하는 모든 이름에 변경된 딕셔너리를 반영
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

# 얕은 복사 : copy() -> 원본가 다른 또다른 딕셔너리를 만드는 것
# 딕셔너리의 키/값을 또다른 딕셔너리로 복사
# 딕셔너리의 모든 키 가져오기
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

# 깊은 복사 : deepcopy()
# 딕셔너리의 모든 키 가져오기
signals = {'green':'go','yellow':'go faster','red':['stop','smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)
# red 요소 하나 변경
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy) # 리스트 요소는 얕은 복사 발생
# 깊은 복사
import copy
# 딕셔너리의 모든 키 가져오기
signals = {'green':'go','yellow':'go faster','red':['stop','smile']}
signals_copy = copy.deepcopy(signals)
print(signals)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy) # 리스트 요소는 얕은 복사 발생

# 딕셔너리의 비교
# 비교 연산자(==, !=)를 사용하여 비교 가능
# 키와 값이 동일해야 True, 순서와 상관없이
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)
# print(a <= b) # <=는 사용 불가

a = {1:[1,2], 2:[1], 3:[1]}
b = {1:[1,1], 2:[1], 3:[1]}
print(a==b)

# 순회하기 : for과 in
# 딕셔너리를 순회시키면 키가 반환
accusation = {'room':'ballroom', 'weapon':'lead pipe', 'person':'Col. Mustard'}
for card in accusation: # or for card in accusation.keys():
    print(card)
# 키가 아닌 값을 순회하려면 values() 사용
for card in accusation.values():
    print(card)
# 키-값 튜플로 반환하려면 items()
for card in accusation.items():
    print(card)
# items()로 반환된 키-값을 다시 다른 변수에 저장하여 사용할 수 있다.
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# 딕셔너리 컴프리헨션
# {키_표현식 : 값 표현식 for 표현식 in 순회 가능한 객체}
word = 'letters'
letter_count = {letter: word.count(letter) for letter in word}
print(letter_count)
# 좀 더 파이써닉한 예제
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in set(word)}
print(letter_counts)
# 딕셔너리 컴프리헨션의 조건문, 다중반복문
# {키_표현식:값_표현식 for 표현식 in 순회 가능한 객체 if 테스트}
vowels = ' aeiou'
word = 'onomatopoeia'
vowel_count = {letter:word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_count)