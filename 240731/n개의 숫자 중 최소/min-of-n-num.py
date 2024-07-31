n = int(input())
arr = list(map(int, input().split()))
count = 0

min_val = arr[0]
for elem in arr[1:]:
     if min_val > elem:
        min_val = elem
for i in arr:
    if i == min_val:
        count += 1

print(min_val, count)