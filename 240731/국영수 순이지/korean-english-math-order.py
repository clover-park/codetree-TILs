class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
members = []
for i in range(n):
    name, kor, eng, math = tuple(input().split())
    members.append(Student(name, int(kor), int(eng), int(math)))

members.sort(key = lambda x : (-x.kor, -x.eng, -x.math))

for p in members:
    print(f'{p.name} {p.kor} {p.eng} {p.math}')