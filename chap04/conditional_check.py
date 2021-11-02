# 1~10 사이의 숫자를 선택해서 secret 변수에 할당, 또다른 숫자는 guess변수에 할당
# guess 변수가 secret 변수보다 작으면 'too low', 크면 'too high', 일치하면 'just right'출력
secret = 10
guess = 4
if guess<secret:
    print('too low')
elif guess>secret:
    print('too high')
else:
    print('just right')


# True나False를 small과 green 변수에 할당
# small과 green을 기준으로 체리, 완두콩, 수박, 호박을 출력
# 예 : 체리는 작고 녹색이 아니다, 완두콩은 작고 녹색이다, 수박은 크고 녹색이다, 호박은 크고 녹색이 아니다.
small = True
green = True
if small:
    if green:
        print('pea')
    else:
        print('cherry')
else:
    if green:
        print('watermelon')
    else:
        print('pumpkin')