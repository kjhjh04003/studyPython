# disaster의 값을 확인하고, 단어 출력
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")


# 중첩 if
furry = True
large = True
if furry:
    if large:
        print("It's a yeti")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human.Or a hairless cat")


# 여러개 조건
color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)
    

# none, 0, 0.0, ' ', [], (), {}, Set() 은 모두 False로 간주


# 여러개 비교 : in
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
# 위의 코드를 더 간단히 하기 위해 멤버십 연산자(in)을 사용
vowels = 'aeiou'
letter = 'o'
print(letter in vowels)
if letter in vowels:
    print(letter, 'is a vowel')


# 바다 코끼리 연산자
# 이름 := 표현식
# 일반적
tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))
# 바다코끼리 연산자 사용
tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))