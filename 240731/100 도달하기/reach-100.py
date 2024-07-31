# arr = [0]*11
# = arr = [0,0,0,0,0,0,0,0,0,0,0]
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
num = int(input())
arr[0] = 1
arr[1] = num
print(arr[0], arr[1], end=' ')

# 3번째 항부터 10번째 항까지 추가
for i in range(2, 12): 
    arr[i] = arr[i - 1] + arr[i - 2]
    print(arr[i], end = ' ')
    if arr[i] > 100:
        break