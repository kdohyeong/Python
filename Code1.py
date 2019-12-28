'''


print("=" * 50)
print("My Program")
print("=" * 50)

multiline=''
Life is too short
You need python
''

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

print("I eat %d apples" %3)
print("I eat %s melons" % 'Four')

number = 10
day = 'five'

print("I ate %d apples. so I was sick for %s days." %(number , day))

print("%10s" % 'Hi')
print("%-10s" % 'Hi')
print("%0.4f" %3.248592)


'''



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
