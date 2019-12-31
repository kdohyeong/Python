## input 의 사용

a = input("출력할 문자를 입력하세요 :")

print(a)

# 문자열의 띄어쓰기는 콤마로 한다.
print("life"+"is"+"too short")
print("life", "is", "too short")

#end=""을 이용하면 매개변수 사이의 끝문자 지정 가능

for i in range(10):
    print(i, end="")

# 파일 생성하기 'r'는 읽기 , 'r'은 쓰기 'a'는 추가
f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'w')
f.close()

# 쓰기모드로 열어 출력값 적기
f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", "w")
for i in range(1,10):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

## readline()함수 이용하기
# 첫번째 줄 출력
f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'r')
line = f.readline()
print(line)
f.close()

# while 루프를 사용하여 한줄씩 읽다가 더이상 없을때 break
f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'r')
while True:
    
    line = f.readline()
    
    if not line: break

    print(line)
f.close()

## readlines() 함수 이용하기
# readlines()는 리스트의 형태로 각 줄을 돌려준다.

f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'r')
lines = f.readlines()

for line in lines:
    print(line)

f.close()

## read() 함수 이용하기
# read()는 전체 내용을 문자열로 반환한다.

f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'r')
data = f.read()

print(data)

f.close()

## 파일에 새로운 내용 추가하기.
f = open("C:/Users/KDHyeong/Desktop/Python/python/test1.txt", 'a')

for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

## with문과 함께 사용하기

f = open("C:/Users/KDHyeong/Desktop/Python/python/foo.txt" , 'w')
f.write("Life is too short, you need python")
f.close()

# with문을 사용하면 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close 되어 편리하다.

with open("C:/Users/KDHyeong/Desktop/Python/python/foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

