n , k = tuple(input().split())
k = int(k)

arr = list(map(int, input().split()))

arr.sort()

print(arr[k-1])