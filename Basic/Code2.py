# 리스트 만들기


a = [1 , 2 , 3 , 4 , 5 , 6]

print(a)
print(a[2])
print(a[4])
print(a[2]+a[5])

# 리스트 속 리스트

a = [1 , 2 , 3 , ['a' , 'b' , 'c'] , ['d' , 'e' , 'f']]

print(a[3])
print(a[4])
print(a[3]+a[4])
print(a[3][2])
print(a[4][1])

# 리스트 슬라이싱

print(a[0:2])  # 순서끝은 포함 x
print(a[0:4]) 
print(a[:2])
print(a[2:])
print(a[3][1:])

# 리스트 연산

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a*3)

print(len(a)) #리스트 길이

a[2] = 7 # 리스트 수정
print(a)

del a[2] #리스트 요소 삭제 del 객체

del b[:2]
print(b)

# 리스트 관련 함수

a.append(6) # 맨 마지막에 추가
print(a)
a.append([5,6,7])
print(a)
a = [1 , 5 , 7 , 2 , 4 , 9 ]
a.sort()
print(a)

a = ['a', 'c' , 'd']

a.reverse() # 리스트 뒤집기
print(a)

print(a.index('a')) # 자리의 위치값 찾기
print(a.index('c'))

a = [1, 2, 3, 1, 2, 3]

a.remove(3) #첫번째로 찾은 요소 지움
print(a)

print(a.pop()) # 맨 마지막 요소 반환 후 제거
print(a)

a = [1, 2, 3, 1, 2, 3]

print(a.pop(2)) # 2번자리 요소 반환 후 제거 
print(a)

print(a.count(2)) # 요소 개수 세기

# 리스트 확장
b = [6 , 7]  
a.extend([3,5,7])  
print(a)
a.extend(b)
print(a)