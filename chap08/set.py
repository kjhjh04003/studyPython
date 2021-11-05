# 셋은 값은 버리고 키만 남으느 딕셔너리와 같다.
# 각 키는 유일해야 한다.
# 셋은 숫서와 상관 없이 저장된다.
# 어떤 것이 존재하는지만 판단할 때 셋을 사용( 리스트는 순서 중요)

# 생성하기 : set()
# 셋을 생성할 때는 set()을 사용하거나 {}안에 콤마로 구분
# 빈 셋을 만들 때 set()
empty_set = set()
print(empty_set)
even_numbers = {0,2,4,6,8}
odd_numbers = {1,3,5,7,9}
print(even_numbers)
print(odd_numbers)

# 변환하기 : set()
# 리스트, 문자열, 튜플, 딕셔너리에서 중복된 값을 삭제하기 위해 셋을 사용한다.
print(set('letterse'))
# 리스트를 셋으로
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon','Dancer']))
# 튜플을 셋으로
print(set(('Ummagumma','Echoes','Atom Heart Mother')))
# 딕셔너리를 셋으로
print(set({'apple':'red','orange':'orange','cherry':'red'}))