import sys
n = int(input())

arr = list(map(int, input().split()))
arr = arr[::-1]

cha = sys.maxsize

for i in range(n):
    for j in range(n):
        if arr[i] - arr[j] > 0 and arr[i] - arr[j] <= cha:
            cha = arr[i] - arr[j]

print(cha)