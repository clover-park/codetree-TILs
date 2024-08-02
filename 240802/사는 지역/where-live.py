class Info:
    def __init__(self, name, address, city):
        self.name = name
        self. address = address
        self.city = city

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Info(name, address, city) for name, address, city in arr]

index = 0

for person in people:
    if person.name > people[index].name:
        index += 1

print(f'name {people[index].name}')
print(f'addr {people[index].address}')
print(f'city {people[index].city}')