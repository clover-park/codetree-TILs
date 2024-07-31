'''
튜플은 값을 수정할 수 없다!!!
수정, 추가, 제거 불가!!!

외우삼. 규칙임.
class 클래스명
객체의 인스턴스를 만들 때 생성자가 call된다.
static method 가 아닌 이상 항상
class 내부 함수의 첫번째 인자는 self이어야 한다.
'''

code, loc, time = tuple(input().split())

class Spy:
    def __init__(self, code, loc, time):
        self.code = code
        self. loc = loc
        self.time = time

a = Spy(code, loc, time)

print(f'secret code : {a.code}')
print(f'meeting point : {a.loc}')
print(f'time : {a.time}')