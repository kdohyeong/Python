# 튜플은 리스트와 거의 동일.

# 튜플은 리스트와 다르게 ()로 둘러싼다.
# 리스트는 값의 생성 삭제 수정 가능 가능 , 튜플은 값 수정이 불가능 **중요

t1 = ()
t2 = (1 , ) #요소를 하나만 가질경우 ,를 뒤에 붙여야 한다.
t3 = (1 , 2 , 3)
t4 = 1, 2, 3  # 괄호를 생략해도 됌

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)

print(t1 + t2)  # 더하기
print(t1 * 3) # 곱셈
print(len(t1)) # 길이구하기

# 딕셔너리
# 연관되는 Key와 Value의 한쌍 

# a = {'key1' : 'Value1', 'key2' : 'value2', 'key3' : 'value3'} 기본형
a = {'name' : 'kdh', 'phone' : '7745', 'birth' : '0303'}

a['university'] = 'CBNU' # 딕셔너리 쌍 추가
print(a)

del a['name'] # 딕셔너리 요소 삭제 [key]
print(a)
## key 값으로 value 얻기
a = {'name' : 'kdh', 'phone' : '7745', 'birth' : '0303'}
print(a['name'])
print(a['birth'])
print(a['phone'])

print(a.keys()) # key 값만 모아 리스트로 반환


#  키 값 하나씩 출력 
for i in a.keys() :
    print(i)

print(list(a.keys())) # a 딕셔너리의 키 값을 리스트화하여 출력

print(a.items()) # key와 value 를 쌍으로 출력

# key값으로 value 출력
# a['name']  = a.get('name') 결과 동일 
# 그러나 없는 key의 경우 a['name']은 오류 a.get('name')은 None 반환
print(a.get('name'))
print(a.get('birth'))
print(a.get('phone'))

