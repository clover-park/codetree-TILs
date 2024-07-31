'''
sort로 정렬을 하려면 대소비교가 가능해야한다.
'''

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
members = []
for i in range(n):
    name, height, weight = tuple(input().split())
    members.append(Person(name, int(height), int(weight)))

members.sort(key = lambda x :x.height)

for p in members:
    print(f'{p.name} {p.height} {p.weight}')