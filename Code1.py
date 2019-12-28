'''


print("=" * 50)
print("My Program")
print("=" * 50)

multiline=''
Life is too short
You need python
''

# 문자 인덱스

a = "Life is too short, You need Python"

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[-5])

b = a[0] + a[1] + a[2] + a[3] + a[4]

c = a[0:10]
print(b)
print(c)

d = "Pithon"

e = d[:1] + 'y' + d[2:] 

print(e)

# 문자 포맷

print("I eat %d apples" %3)
print("I eat %s melons" % 'Four')

number = 10
day = 'five'

print("I ate %d apples. so I was sick for %s days." %(number , day))

print("%10s" % 'Hi') # 열칸 띄고 스트링
print("%-10s" % 'Hi') # 뒤에서부터 열칸 띄고 스트링
print("%0.4f" %3.248592)



# 포맷팅 함수

print("I eat {0} apples.".format(3))
print("I eat {0} melons.".format("Four"))
number = 7
print("I eat {0} orange.".format(number))
day = 10
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print("{0:<15}".format("Hi"))
print("{0:>15}".format("Hello"))
print("{0:^15}".format("Python"))
print("{0:=>15}".format("Destiny"))
print("{0:=^15}".format("KDHyeong"))

name = 'Kimdohyeong'
age = 26

print(f'My name is {name} i am {age} years old')

'''

a = "hobby"
print(a.count('b'))
print(a.find('b')) # 찾는 문자열이 존재하지 않을경우 -1 반환
print(a.index('b')) # 찾는 문자열이 존재하지 않을경우 오류발생
# join
print(",".join('abcd'))  
print(','.join(['a' , 'b' , 'c' , 'd']))

print(a.upper()) # 소문자 -> 대문자

print(a.lower()) # 대문자 -> 소문자

b = "Life is too short, You need too Python"
print(b.split())  # 공백기준으로 쪼개기
print(b.split(',')) # , 기준으로 쪼개기

