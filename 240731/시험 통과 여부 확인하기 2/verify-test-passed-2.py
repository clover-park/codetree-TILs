count = int(input())
avr_score = 0
pass_student = 0

for i in range(count):
    score = map(int, input().split())
    avr_score = sum(score)/4
    if avr_score >= 60:
        print('pass')
        pass_student += 1
    else:
        print('fail')

print(pass_student)