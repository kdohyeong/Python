## 4장 연습문제

#1 자연수가 홀짝인지 판별 함수 만들기
a = int(input("홀짝을 판별할 자연수를 입력하세요 :"))

def is_odd(a):
    if a % 2 == 0 :
        print("짝수 입니다.")
        return
    elif a % 2 == 1 :
        print("홀수 입니다.")
        return
    else :
        print("잘못입력하셨습니다.") 

is_odd(a)

#2 입력으로 들어오는 모든 수의 평균 값을 구하는 함수 만들기


def Average(*args):
    
    result = 0
    for i in args:
        result = result + i 
    result = result / len(args)
    return result
a = Average(1,2,3,4,5)
b = Average(4,5,7,3,6,5)

print(a)
print(b)

#3 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.

f = open("C:/Users/KDHyeong/Desktop/Python/python/test.txt" , 'a')
a = input("텍스트 파일에 입력할 내용 :")
f.write(a)
f.write('\n')
f.close()

f = open("C:/Users/KDHyeong/Desktop/Python/python/test.txt" , 'r')
text = f.read()
print(text)
f.close()

#4 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

f = open("C:/Users/KDHyeong/Desktop/Python/python/test2.txt" , 'r')
text = f.read()
f.close()

f = open("C:/Users/KDHyeong/Desktop/Python/python/test2.txt" , 'w')
f.write(text.replace('java','python'))
f.close()