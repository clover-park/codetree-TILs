arr = list(map(int, input().split()))

count = 0
sum_i = 0
for i in arr:
    if i < 250:
        count += 1
        sum_i += i
    else:
        break # 조기탈출

print(f'{sum_i} {sum_i/count:.1f}')