class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


students = []
for _ in range(5):
    name, score = tuple(input().split())
    students.append(Student(name, int(score)))

min_idx = 0

for i in range(5):
    if students[i].score < students[min_idx].score:
        min_idx = i

print(students[min_idx].name, students[min_idx].score)