# arr = [0]*11
# = arr = [0,0,0,0,0,0,0,0,0,0,0]
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = list(map(int, input().split()))
arr[1] = num[0]
arr[2] = num[1]
print(arr[1], arr[2], end=' ')

# 3번째 항부터 10번째 항까지 추가
for i in range(3, 11): 
    arr[i] = arr[i - 1] + arr[i - 2]
    print(arr[i]%10, end = ' ')