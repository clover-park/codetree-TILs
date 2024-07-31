n = int(input())
arr = []
mul = 1
count = 0

for i in range(1, 1000):
    mul = n*i
    if mul % 5 == 0:
        count += 1
    elif count == 2:
        break
    arr.append(mul)


for i in arr:
    print(i, end=' ')