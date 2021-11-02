# str() : 다른 데이터 타입을 문자열로 변환
print(str(98.6))
print(str(1.0e4))
print(str(True))

# 이스케이프 문자 : \
# \n : 줄바꿈
palindrome = 'A man, \nA plan, \nA canal:\nPanama.'
print(palindrome)
# \t : tab(공백)
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')
# 원시 문자열은 이스케이프 문자를 무효화
info = r'Type \n to get a new line in a normal string'
print(info)


# 결합하기(+)
# 리터럴 문자열 또는 문자열 변수를 결합
print('Release the kraken! ' + 'No, wait!')
# 이어서 사용
print("My word! " "A gentleman caller!")
print("Alas! ""The kraken!")
# 괄호 사용
vowels = ('a'
       "e"'''i'''
       'o' """u""")
print(vowels)

# 복제하기(*)
# 문자열을 복제
start = 'Na ' * 4 + '\n'
middle = 'Hey ' *3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# 문자열 추출([])
# 문자열에서 한 문자를 얻기 위해서는 문자열 이름 뒤에 대괄호와 오프셋을 지정
# 가장 왼쪽 오프셋은 0, 가장 오른쪽의 오프셋은 -1
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])
# 문자열 길이 혹은 그 이상의 오프셋으로 지정하면 오류발생
#   print(letters[100])
# 문자열은 불변하기 때문에 특정 인덱스에 문자를 삽입하거나 변경할 수 없다.
name = 'Henny'
#   name[0] = 'P'
# replace()나 슬라이스와 같은 문자열 함수를 사용할 수 있다. -> 실제 변수값에 영향을 주지 않는다.
name = 'Henny'
print(name.replace('H', 'P'))
name = 'Henny'
print('P' + name[1:])

# 슬라이스로 부분 문자열 추출
# 슬라이스를 사용하여 한 문자열에서 문자열 일부를 추출할 수 있다.
# 대괄호를 사용하여 시작 오프셋, 끝 오프셋, 옵션으로 스텝을 명시하여 슬라이스를 정의한다.
# [:] : 처음부터 끝
# [start:] : start부터 끝까지
# [:end] : 처음부터 end-1까지
# [start : end] : start부터 end-1까지
# [start : end : step] : step만큼 문자는 건너 띄면서, start부터 end-1까지
letters = 'abcdefghijklmnopqrstuvwxyz'
print('[:]', letters[:])
print('[20:', letters[20:]) # 오프셋 20부터 끝까지
print('[10:]', letters[10:])
print('[12:14]', letters[12:15])
print('[-3:]', letters[-3:]) # 마지막 세 문자
print('[18:-3]', letters[18:-3])
print('[-6:-2]', letters[-6:-2])
# 1보다 큰 스텝을 원한다면
print('7스텝 ', letters[::7])
print(letters[4:20:3])

# 문자열 길이(len())
# 문자열 길이를 센다.
print(len(letters))
empty=""
print(len(empty))

# 문자열 나누기(split())
# 어떤 구분자를 기준으로 하나의 문자열을 작은 문자열들의 리스트로 나누기 위해 사용
tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
print(tasks.split(','))
print(tasks)
print(tasks.split()) # 구분자가 없으면 공백 문자를 사용

# 문자열 결합하기(join())
# 문자열 리스트를 하나의 문자열로 결합
crypto_list = ['Yeti', 'Bigfoot', 'Loch NessMonster']
crypto_string = ','.join(crypto_list)
print(crypto_list)
print('Found and signing book deals:', crypto_string)

# 문자열 대체하기(replace())
# 문자열 일부를 대체
# 원본 문자열 수정x
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a ', 'a famous ', 100)) # 100회까지 바꾼다.

# 문자열 스트립(strip())
# 문자열 맨 앞, 맨 뒤에서 패딩문자를 제거하는 것
# 왼쪽만 제거 : lstript(), 오른쪽만 제거 : rstrip()
world = " earth "
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())
print(world.strip('!'))
blurt="What the...!!?"
print(blurt.strip('.?!'))

# 검색과 선택
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
# startswith() : 해당 문자열로 시작하는가
print(poem.startswith('All'))
# endswith() : 해당문자열로 끝나는가
print(poem.endswith('Than\'s all, folks!'))
# fine() : 어떤 문자열에서 부분 문자열 오프셋 찾기, 찾지 못하면 -1반환
# index() : 어떤 문자열에서 부분 문자열 오프셋 찾기, 찾지 못하면 오류 발생
# 문자열의 처음에서부터 찾기
word = 'the'
print(poem.find(word))
print(poem.index(word))
# 문자열의 끝에서부터 찾기
print(poem.rfind(word))
print(poem.rindex(word))
# 부분 문자열 없을 경우
word = 'duck'
print(poem.find(word))
print(poem.rfind(word))
# print(poem.index(word))
# print(poem.rindex(word))
# 문자열 개수
word = 'the'
print(poem.count(word))
# 알파벳 또는 숫자로 이루어져 있는가?
print(poem.isalnum())

# 대소문자
setup = 'a duck goes into a bar...'
# 양끝 . 없애기
print(setup.strip('.'))
# 첫 단어 대문자로
print(setup.capitalize())
# 모든 단어의 첫 글자를 대문자로
print(setup.title())
# 글자를 모두 대문자로
print(setup.upper())
# 글자를 모두 소문자로
print(setup.lower())
# 대문자는 소문자로, 소문자는 대문자로
print(setup.swapcase())

# 정렬
# 지정된 공간에서 중앙 정렬
print(setup.center(30))
# 왼쪽 정렬
print(setup.ljust(30))
# 오른쪽 정렬
print(setup.rjust(30))


# 포매팅
# 옛스타일 : %
# format_string % data 형식
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)

actor = 'RichardGere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)   # 12 공간을 기준으로 오른쪽정렬 
print('%+12s' % thing)  # 12 공간을 기준으로 오른쪽정렬
print('%-12s' % thing)  # 12 공간을 기준으로 왼쪽정렬
print('%.3s' % thing)   # 숫자-1 오프셋 만큼
print('%12.3s' % thing) # 숫자-1 오프셋 만큼을 오른쪽 정렬
print('%-12.3s' % thing)

thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12s' % thing)  # 12 공간을 기준으로 왼쪽정렬
print('%.3s' % thing)   # 숫자-1 오프셋 만큼
print('%12.3s' % thing) # 숫자-1 오프셋 만큼을 오른쪽 정렬
print('%-12.3s' % thing)

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)  # 12 공간을 기준으로 왼쪽정렬
print('%.3d' % thing)   # 숫자-1 오프셋 만큼
print('%12.3d' % thing) # 숫자-1 오프셋 만큼을 오른쪽 정렬
print('%-12.3d' % thing)

# 새스타일({}, format())
# format_string.format(data) 형식
thing = 'woodchuck'
print('{}'.format(thing))
place = 'lake'
print('The {} is in the {}'.format(thing, place))
print('The {1} is in the {0}'.format(place, thing))
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))
# 딕셔너리로도 사용 가능
d = {'thing':'duck', 'place':'bathtub'}
print('The {0[thing]} is in the {0[place]}'.format(d))

thing='wraith'
place='window'
print('The {} is at the {}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing,place)) # < 왼쪽정렬
print('The {:^10s} is at the {:^10s}'.format(thing,place)) # ^ 가운데 정렬
print('The {:>10s} is at the {:>10s}'.format(thing,place)) # > 오른쪽 정렬
print('The {:!^10s} is at the {:!^10s}'.format(thing,place)) # 가운데 정렬 후 공백은 !로 채우기

# 최신 스타일:f-문자열
# 첫 인용 부호 앞에 문자 f또는 F를 입력, 변수 이름이나 삭을 중괄호 안에 포하맿 값을 문자열로 가져온다.
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')
print(f'{thing = }, {place =}')
print(f'{thing[-4:] =}, {place.title() =}')
