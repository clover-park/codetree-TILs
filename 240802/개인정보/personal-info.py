class Student:
    def __init__(self, name, height, weight):       
        self.name = name
        self.height = int(height)
        self.weight = weight


students = []

for student_id in range(0, 5):
    name, height, weight = tuple(input().split())
    students.append(Student(name, height, weight))

students.sort(key = lambda x : (x.name))

print('name')

for p in students:
    print(f'{p.name} {p.height} {p.weight}')

students.sort(key = lambda x : (-x.height))

print('\nheight')

for p in students:
    print(f'{p.name} {p.height} {p.weight}')