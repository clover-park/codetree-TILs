n = int(input())

arr = list(map(int, input().split()))
sort_arr = []

for i in range(n):
    sort_arr.append(arr[i])
    if (i+1) % 2 != 0:
        sort_arr.sort()
        print(sort_arr[i//2], end=' ')