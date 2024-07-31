arr = list(map(int,input().split()))
for i in arr:
    if i == 0:
        arr.pop()
        break
     
for num in reversed(arr):
    print(num, end = ' ')