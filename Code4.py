# 2장 연습문제
#1 a,b,c의 평균
a = 80
b = 75
c = 55

print("평균은 ", (a + b + c) / 3)

#2 13의 홀or짝 판단
if 13 % 2 == 1 :
    print("13은 홀수입니다.")
else :
    print("13은 짝수입니다.")

#3 홍길동씨 주민 881120 - 1068234 를 연월일 그리고 나머지로 슬라이싱

H = "881120-1068234"

print("홍길동씨의 생년월일은", H[:6] ,"입니다.")
print("홍길동씨의 주민번호 뒷자리는", H[7:], "입니다.")

#4 주민번호의 성별을 나타내는 숫자 출력

if H[7] == '1' :
    print("뒷자리가 1로 시작하므로 남자입니다.")
elif H[7] == '2' :
    print("뒷자리가 2로 시작하므로 여자입니다.") 
else : 
    print("주민번호에 오류가 있습니다.")

#5 a:b:c:d 를 replace 함수로 a#b#c#d 로 대체

a = 'a:b:c:d'

print(a.replace(':' , '#')) # replace 함수 사용법 숙지

#6 [1, 3, 5, 4, 2] 를 [5, 4, 3, 2, 1] 로 만들기

a = [1, 3, 5, 4, 2]

a.sort()
a.reverse()
print("정렬완료된 리스트" , a)

#7 ['Life', 'is', 'too', 'short'] 를 문자열로 변환

a = ['Life', 'is', 'too', 'short']

print("문자열로 변환" , (" ".join(a)))  #join 함수 사용법 숙지

#8 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.

t1 = (1, 2, 3) 
print(t1 + (4,))

#9 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.

a = {'A':90, 'B':80, 'C':70} 

print(a['B'])
print(a.get('B'))
print(a.pop('B')) #3가지 방법

# 10 a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

print(list(set(a)))

# 11 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

a = b = [1, 2, 3]
a[1] = 4
print(b)

# [1, 4, 3]이 출력된다. 
# a와 b 변수는 모두 동일한 [1, 2, 3]이라는 리스트 객체를 가리키고 있기 때문이다.