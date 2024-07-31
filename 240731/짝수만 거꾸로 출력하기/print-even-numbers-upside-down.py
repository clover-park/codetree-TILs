count = int(input())
num = map(int, input().split())
arr =[]

for n in num:
    if n % 2 == 0:
        arr.append(n)
arr = reversed(arr)

for i in arr:
    print(i, end = ' ')