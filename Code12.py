def add(a, b):
    return a + b


def sub(a, b):
    return a - b
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)


# 오류 발생 해결을 위해서는
if __name__ == "__main__" :

    print(add(1, 4))
    print(sub(4, 2))

# 이 문장에서 실행되려면 직접 실행할 때에만 수행 모듈로 이용되면 수행되지 않는다.
