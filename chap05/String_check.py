# m으로 시작하는 단어를 대문자로 만들기
# 다음에--------------
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.startswith('m'))

# 형식에 맞춰 각 리스트의 질문과 답을 차례로 출력하기
# 다음에--------------
questions = ["We don't serve strings around here. Are you a string?",
            "What is said on Father's Day in the forest?",
            "What makes the sount 'Sis! Boom! Bah!'?"
            ]
answers = ["An exploding sheep.",
          "No, I'm a frayed knot.",
          "'Pop!' goes the weasel."
          ]

# 옛 스타일 포매팅을 사용하여 시 쓰기
# 'roast beef', 'ham', 'head', 'clam'을 아래 문자열에 대체
print('My kitty cat likes %s,' % 'roast beef')
print('My kitty cat likes %s, ' % 'ham')
print('My kitty cat fell on his %s And now thinks he\'s a %s.' % ('head', 'clam'))

# 새 스타일의 포매팅을 사용하여 메일 쓰기
letter = """Dear {saluttation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it should never be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""
print(letter.format(saluttation='', name='Mr.Jun', product='fan', verbed='verbed', room='5-4', animals='rabbit',
             amount='$55.2', percent='98', spokesman='Mr.Lee', job_title='lawyer'))

# 옛 스타일
name = ['duck', 'gourd', 'spitz']
for n in name:
    n = n.capitalize()
    print('%sy Mc%sface' % (n,n))

# format()
name = ['duck', 'gourd', 'spitz']
for n in name:
    n = n.capitalize()
    print('{}y Mc{}face'.format(n,n))

# 최신 스타일
name = ['duck', 'gourd', 'spitz']
for n in name:
    n = n.capitalize()
    print(f'{n}y Mc{n}face')