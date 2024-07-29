# 배열을 뒤집을 때 [::-1]
# reverse()보다 빠르다.

arr = input().split()

reverse_arr = arr[::-1]

for i in reverse_arr:
    print(i, end = '')