## for 문

#기본형
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

#기본적인 for문과 조건문의 혼합
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

# for i in range() 형태
# range(a,b) -> a이상 b 미만 범위 객체

# for와 range 함수를 이용한 구구단

for i in range (2, 10):
    print(" ")
    for j in range (1, 10):
        print(i * j, end=" ")

print(" ")

#리스트내 for문 사용
a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i * 3)
print(result)

#리스트 내포 일반문법 [표현식 for 항목 in 반복가능객체 if 조건문]

a = [x*y for x in range(2,10)
         for y in range(1,10)]

print(a)