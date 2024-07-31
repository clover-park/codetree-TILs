arr = list(map(int,input().split()))
new_arr = []

for i in arr:
    new_arr.append(i)
    if i == 0:
        new_arr.pop()
        break

     
for num in reversed(new_arr):
    print(num, end = ' ')