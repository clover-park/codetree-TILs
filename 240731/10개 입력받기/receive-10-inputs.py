arr = map(int, input().split())
new_arr = []
count = 0

for i in arr:
    new_arr.append(i)
    if i == 0:
        new_arr.pop()
        break
    count += 1

sum_arr = sum(new_arr)
avr_arr = sum_arr/count

print(f'{sum_arr} {avr_arr:.1f}')