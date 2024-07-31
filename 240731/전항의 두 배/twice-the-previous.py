list = list(map(int, input().split()))
a1 = list[0]
a2 = list[1]
print(a1, a2, end=' ')
arr = [a1, a2]

for i in range(2,10):
    arr.append(arr[i-1] + 2*arr[i-2])
    print(arr[i], end=' ')