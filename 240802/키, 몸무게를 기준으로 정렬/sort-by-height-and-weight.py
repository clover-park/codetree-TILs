class Student:
    def __init__(self, name, height, weight):       
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
students = []

for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), int(weight)))

students.sort(key = lambda x : (x.height, -x.weight))

for p in students:
    print(p.name, p.height, p.weight)