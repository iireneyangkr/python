# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))

# index는 0부터 시작 - 2진수가 0, 1로 이루어지기 때문
print(list_a[0])
print(list_a[1])
print(list_a[2])

# [0:1] 구간 출력
print(list_a[0:1])
print(list_a[0:2])
print(list_a[0:3])

# # append - 요소 더하기
list_a.append(4)
print(list_a)
#
# # remove - 요소 빼기
list_a.remove(2)
print(list_a)
#
# # clear - 전체 삭제
list_a.clear()
print(list_a)


# tuple (1, ) - 생성 후 값 변경 불가
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))

# dict (map) - {"key" : "value"}
dict_a ={"apple" : "a type of fruits", "pen" : "a thing to write"}
print(dict_a)
print(dict_a["apple"])
print(dict_a["pen"])
dict_a["pen"] = "something to write"
print(dict_a["pen"])

# set set ([]) - 자동 중복 제거!!!
set_a = set([1, 2, 3, 3, 3, 2])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 교집합, 합집합, 차집합, 여집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
