n = int(input())

offset = 100

arr = [0] * (205)

for _ in range(n):
    s, e = tuple(map(int, input().split()))

    for i in range(s + offset, e + offset):
        arr[i] += 1

print(max(arr))