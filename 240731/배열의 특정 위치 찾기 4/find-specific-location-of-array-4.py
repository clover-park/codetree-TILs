arr = map(int, input().split())
even_num = []
count = 0

for i in arr:
    if i % 2 == 0 and i != 0:
        even_num.append(i)
        count += 1
    elif i == 0:
        break

sum_arr = sum(even_num)

print(count ,sum_arr)