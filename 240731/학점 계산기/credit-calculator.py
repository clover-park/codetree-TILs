# 나눗셈은 되도록 쓰지 않는다.
# 0으로 나눌 수도 있기 때문, 0으로 나눌 경우 에러가 뜬다.

count = int(input())
score = map(float, input().split())
grade = sum(score) / count

print(f'{grade:.1f}')

if grade >= 4.0:
    print('Perfect')
elif grade >= 3.0:
    print('Good')
else:
    print('Poor')