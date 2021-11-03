# while
count = 1   # 카운터 변수
while count <= 5:   # 조건에 만족되지 않으면 반복 종료
    print(count)
    count += 1

# break
# 어떤 일이 언제 일어나는지 확실하지 않다면 무한반복문에 break문을 사용
# while True:
#     stuff = input('String to capitalize [type q to quit]: ')
#     if stuff == "q": # 입력문자열이 q면 반복문 종료
#         break
#     print(stuff.capitalize()) # 한 라인을 읽은 후 첫 문자를 대문자로 출력
    
# continue
# 반복문을 중단하지 않지만 몇몇 이유로 다음 반복을 건너뛰고 싶을 때 사용
# while True:
#     value = input('Integer, please [q to quit] ')
#     if value == 'q': #종료
#         break
#     number = int(value)
#     if number % 2 == 0: # 짝수
#         continue # 건너띄기
#     print(number, "squared is", number*number) # 홀수일 때, 그 수의 제곱

# break 확인:else
# while문을 모두 실행하였지만 break 할 내용을 발견하지 못했을 때는 else문이 실행
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:   # break문이 호출되지 않은 경우
    print('No even number found')


