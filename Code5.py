# 제어문
# 조건부 표현식

score = 70
if score >= 60 :
    message = "success"
else :
    message = "Failure"

print(message)

#위의 조건문은 조건부 표현식으로 변환하기

# 조건문이 참인 경우 if 조건문 else 조건문이 참이 아닌경우

message = "success" if score >= 70 else "Failure"

# while 문
# 조건문이 참인 동안에 while 문을 반복 수행

treehit = 0
while treehit < 10 :
    treehit = treehit +1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print("나무가 넘어갑니다.")

# 기본 사용
number = 0
prompt = '''
    1. Add
    2. Del
    3. List
    4. Quit

    Enter number:
    4를 입력시 다음으로 넘어갑니다.
    '''
    
while number != 4:

    print(prompt)
    
    number = int(input())

# while문 강제로 빠져나가기
coffee = 30 
money = int(input("100원 아메리카노 자판기 지불한 금액 입력:"))
remoney = money

while True :
    coffeeorder = int(input("주문할 커피의 개수 입력:"))
    if money <= 100 * coffeeorder :
        print("지불한 금액이 모자릅니다.")
    
    if coffeeorder > 30 :
        print("자판기에 커피가 30잔밖에 없습니다.")
        break
    if coffeeorder > coffee :
        print("자판기에 커피가 %d잔밖에 없습니다."%coffee)
        print("잔 돈 %d원을 반환 후 종료합니다."%remoney)
        break
    if remoney < 100 :
        print("잔 돈이 부족하여 %d원을 반환 후 종료합니다."%remoney)
        break
    if coffeeorder * 100 <= remoney :
        print("주문하신 100원 아메리카노 %d잔 나왔습니다." %coffeeorder)
    if coffee <= 0: 
        print("커피가 모두 소진되었습니다.")
        break
    if coffeeorder * 100 > remoney :
        print("잔 돈이 부족하여 %d원을 반환 후 종료합니다."%remoney)
        break

    remoney -= coffeeorder*100
    coffee -= coffeeorder
    print("자판기에 남은 커피양: %d" %coffee)
    print("남은 돈 %d 입니다." %remoney)
    

    ###break 를 사용하여 while 루프를 벗어난다.

# while 문의 처음으로 돌아가기

a = 0
print("10보다 작은 자연수 중 홀수만 출력")

while a < 10 :
    a += 1

    if a % 2 == 0: continue  # continue를 이용하여 whlie문의 처음으로 돌아감.

    print(a)

## while 무한루프에 빠진 경우 Ctrl + c 버튼을 이용하여 빠져나간다.


