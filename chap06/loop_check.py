# for문으로 리스트[3,2,1,0]출력
# lst = list()
# for n in range(3,-1,-1):
#     lst.append(n)
# print(lst)

# guess_meㄹ 변수에 7을 할당, number 변수에 1 할당
# while문을 이용하여 비교
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number > guess_me:
        print("oops")
        break
    else:
        print("found it!")
        break
    number += 1

# guess_me 변수에 5할당
# for문을 사용하여 range(10)에서 number변수를 사용
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('opps')
        break