'''
enumerate 함수는 i, elem 값을 순차적으로 반환해줍니다.
(순서가 바뀌면 절대 안됩니다)
'''
class Info:
    def __init__(self, name, address, city):
        self.name = name
        self. address = address
        self.city = city

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Info(name, address, city) for name, address, city in arr]

index = 0

for i, person in enumerate(people):
    if person.name > people[index].name:
        index = i

print(f'name {people[index].name}')
print(f'addr {people[index].address}')
print(f'city {people[index].city}')