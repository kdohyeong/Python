# ����Ʈ �����


a = [1 , 2 , 3 , 4 , 5 , 6]

print(a)
print(a[2])
print(a[4])
print(a[2]+a[5])

# ����Ʈ �� ����Ʈ

a = [1 , 2 , 3 , ['a' , 'b' , 'c'] , ['d' , 'e' , 'f']]

print(a[3])
print(a[4])
print(a[3]+a[4])
print(a[3][2])
print(a[4][1])

# ����Ʈ �����̽�

print(a[0:2])  # �������� ���� x
print(a[0:4]) 
print(a[:2])
print(a[2:])
print(a[3][1:])

# ����Ʈ ����

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a*3)

print(len(a)) #����Ʈ ����

a[2] = 7 # ����Ʈ ����
print(a)

del a[2] #����Ʈ ��� ���� del ��ü

del b[:2]
print(b)

# ����Ʈ ���� �Լ�

a.append(6) # �� �������� �߰�
print(a)
a.append([5,6,7])
print(a)
a = [1 , 5 , 7 , 2 , 4 , 9 ]
a.sort()
print(a)

a = ['a', 'c' , 'd']

a.reverse() # ����Ʈ ������
print(a)

print(a.index('a')) # �ڸ��� ��ġ�� ã��
print(a.index('c'))

a = [1, 2, 3, 1, 2, 3]

a.remove(3) #ù��°�� ã�� ��� ����
print(a