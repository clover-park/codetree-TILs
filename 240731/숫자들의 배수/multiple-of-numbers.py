n = int(input())
arr = []
mul = 1
count = 0

for i in range(1, 1000):
    mul = n*i
    arr.append(mul)

for mul in arr:
    print(mul, end=' ')
    if mul % 5 == 0:
        count += 1
    if count >= 2:
        break