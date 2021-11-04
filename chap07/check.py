# year_lists 만들기
# 출생년도를 첫 번째 요소로 하고 1년씩 증가해 다섯 번째 생일이 되는 해까지 요소 넣기
year_lists = [1996, 1997, 1998, 1999, 2000, 2001]
print(year_lists)

# year_lists의 세번째 생일은 몇년도인가
print(year_lists[3])

# year_list 중 가장 나이가 많을 때는 몇년도인가?
print(year_lists[-1])

# things 리스트 만들기
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# things 리스트에서 사람 이름의 첫 글자를 대문자로 바꿔서 출력
# 리스트의 요소가 변경되는가? -> 안바뀜
print(things[1].title())
print(things)

# things 리스트에서 치즈 요소를 모두 대문자로 바꿔서 출력
print(things[0].upper())

# things 리스트에서 질병 요소가 있다면 제거한 뒤 리스트 출력
things.remove('salmonella')
print(things)

# surprise 리스트 만들기
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)

# surprise 리스트의 마지막 요소를 소문자로 변경
# 단어를 뒤집은 다음에 첫 글자를 대문자로
print(surprise[-1].lower()) # 마지막 요소 소문자로 변경
print(surprise[-1].lower()[::-1]) # 단어 뒤집기
print(surprise[-1].lower()[::-1].title()) # 첫 글자 대문자

# 리스트 컴프리헨션 사용하여 range(10)에서 짝수 리스트 만들기
even = [number for number in range(10) if number%2==0]
print(even)

#
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
# start의 각 문자열을 출력
# 첫 글자는 대문자, 각 단어 뒤에 느낌표와 공백 출력
# rhymes의 첫 번째 문자열의 단어 역시 첫 글자를 대문자로 만들고 느낌표 출력
first = [sttr.title() for sttr in start1]
print("%s! %s! %s! %s!" % (first[0],first[1], first[2], rhymes[0][0].title()))
# str2와 공백을 출력
# 두번째 문자열과 마침표 출력
print(start2)