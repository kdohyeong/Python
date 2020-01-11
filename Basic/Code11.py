class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second


    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result




a = FourCal(4,2)

print(type(a))

a = FourCal(4,2)
print(a.setdata(4,2))

FourCal.setdata(a, 4, 2)

a = FourCal(4,2)


a.setdata(4,2)

print(a.first)
print(a.second)

a = FourCal(4,2)

b = FourCal(3,8)

a.setdata(4, 2)

print(a.first)

b.setdata(3, 7)


print(b.first) 
print(a.first)
# a객체의 first값은 b객체의 first값의 영향을 받지 않고 원래 값을 유지하고 있다.
print(id(a.first))
print(id(b.first))

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

print(b.add())
print(b.mul())
print(b.div())
print(b.sub())

 # 클래스의 상속
 # 기존 클래스를 변경하지 않고 기능을 추가할 때 사용 
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)

print(a.add())
print(a.div())

print(a.pow())

# 매서드 오버라이딩 (덮어씌우기)
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())


# 클래스의 변수  클래스이름.클래스 변수
class Family:
    lastname = "김"


print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
