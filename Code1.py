print("=" * 50)
print("My Program")
print("=" * 50)

multiline='''
Life is too short
You need python
'''

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