# 3장 연습문제

#1 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

a = 1
b = 0
while True:
    if a % 3 ==0:
        b = b + a
    a = a+1
    if a % 3 ==0:
        b + a
    if a >= 1000:
        break
print(b)

#2 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

a = 0
while a < 6:
    print("*" * a) 
    a = a + 1

#3 for 문을 사용해 1부터 100까지의 숫자를 출력해보자

for i in range (1, 101):
    print(i)

#4 A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

#[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

#for문을 사용하여 A 학급의 평균 점수를 구해 보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in score:
    sum = sum + i

print(sum / len(score))

#5  리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

#numbers = [1, 2, 3, 4, 5]
#result = []
#for n in numbers:
    #if n % 2 == 1:
       #result.append(n*2)
#위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

numbers = [1, 2, 3, 4, 5]
result = []

a = [n*2 for n in numbers if n % 2 ==1]

print(a)


