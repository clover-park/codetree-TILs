n, k = tuple(map(int, input().split()))

arr = [0] *(n+1)
for _ in range(k):
    s, e = tuple(map(int, input().split()))
    for i in range(s, e+1):
        arr[i] += 1

print(max(arr))