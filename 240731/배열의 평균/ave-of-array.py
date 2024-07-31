arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

sum_row_1 = 0
sum_row_2 = 0
sum_column_1 = 0
sum_column_2 = 0
sum_column_3 = 0
sum_column_4 = 0
sum_all = 0

for i in range(2):
    sum_column_1 += arr_2d[i][0]
    sum_column_2 += arr_2d[i][1]
    sum_column_3 += arr_2d[i][2]
    sum_column_4 += arr_2d[i][3]

for j in range(4):
    sum_row_1 += arr_2d[0][j]
    sum_row_2 += arr_2d[1][j]

for i in range(2):
    for j in range(4):
        sum_all += arr_2d[i][j]

print(sum_row_1/4, sum_row_2/4)
print(sum_column_1/2, sum_column_2/2, sum_column_3/2, sum_column_4/2)
print(f'{sum_all/8:.1f}')