#함수 연습

def add(a, b):
    return a + b

a = 3

b = 4

c= add(a, b) # a, b는 매개변수

print(c)  
print(add(3,4)) # 3, 4는 인수

def add2 (a,b):
    result = a + b
    return result

#입력값이 없는 함수 
def say():
    return "Hi"

a = say()

print(a)

# 결과 값이 없는 함수

def add3(a, b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a + b))

a= add(3,4)
print(a)

# 입력값도 결괏값도 없는 함수
def say2():
    print("Hi")

say()

# 여러 개의 입력값을 받는 함수 만들기

def add_many(*args):  # *args는 arguments의 약자 관례적으로 사용
    result = 0
    for i in args:
        result = result + i
    return result

a = add_many(1,2,3,4,5)

print(a)

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
        return result
    if choice =='mul':
        result = 1
        for i in args:
            result = result * i
        return result

result = add_mul('add', 1,4,5,6)
print(result)
result = add_mul('mul', 1,4,5,6)
print(result)

# 키워드 파라미터 ** 은 딕셔너리 형태로 줌.
def print_kwargs(**kwargs):     
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 리턴값에 두가지를 썼을때
def add_and_mul(a,b): 
    return a+b, a*b

a = add_and_mul(3,4)
print(a) #출력하면 튜플의 형식으로 반환해준다.

# return의 다른 쓰임새
# 특정한 상황일 때 함수를 빠져나가고 싶으면 단독으로 return을 사용
def say_nick(nick):
    if nick =='바보':
        return
    print("나의 별명은 %s 입니다." %nick)
say_nick('바보') #바보의 경우 return 으로 빠져나가 출력이 되지않는다.

say_nick('야호')

#매개변수 값을 미리 설정한 경우
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself('kdh',26)
say_myself('jeny',23,False)
# 매개변수의 값을 미리 설정할 때에는 맨 뒤에 위치시켜야 오류가 발생하지 않는다.

## lambda
# 함수를 생성할 때 사용하는 예약어로 간결하게 만들때 def 대신 사용

add = lambda a, b : a+b  #lambda의 기본 형식 lambda 매개변수 : 표현식 
result = add(3, 4)  
print(result)

