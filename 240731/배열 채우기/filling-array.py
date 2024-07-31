arr = list(map(int,input().split()))
new_arr = []

for i in arr:
    new_arr.append(i)
    if i == 0:
        break
new_arr.pop()
     
for num in reversed(new_arr):
    print(num, end = ' ')