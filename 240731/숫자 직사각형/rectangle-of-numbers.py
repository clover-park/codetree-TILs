arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num=1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        print(arr_2d[i][j], end=" ")
        num += 1
    print()