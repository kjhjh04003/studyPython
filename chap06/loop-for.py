# 반복문(iterator)
# for 과 in
# while문
word = 'thud'
# offset = 0
# while offset < len(word):
#     print(word[offset])
#     offset += 1

# for문 대체
# for letter in word:
#     print(letter)

# break
# for letter in word:
#     if letter == 'u':
#         break
#     print(letter)

# break문 확인:else
# for letter in word:
#     if letter == 'x':
#         print("Eek! An 'X'!")
#         break
#     print(letter)
# else:
#     print("No 'x' in there.")

# 숫자 시퀀스 생성 : range()
# range() : 리스트나 튜플 같은 자료구조를 생성하여 저장하지 않더라도 특정 범위 내에서 숫자 스트림을 반환
# range(시작, 끝, 스텝) 형식
# 시작은 생략 가능하며, 생략하면 0부터 시작, 끝은 꼭 입력해야 한다.
for x in range(0,3):
    print(x)
print(list(range(0,3)))
for x in range(2,-1,-1):
    print(x)
print(list(range(2,-1,-1)))
print(list(range(0,11,2)))