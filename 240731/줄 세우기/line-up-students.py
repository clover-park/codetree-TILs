class Student:
    def __init__(self, height, weight, student_id):
        self.height = height
        self.weight = weight
        self.student_id = student_id

n = int(input())
students = []

for student_id in range(1, n+1):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, student_id))

students.sort(key = lambda x : (-x.height, -x.weight, x.student_id))

for p in students:
    print(f'{p.height} {p.weight} {p.student_id}')