'''
arr = input().split()

sum_val = 0 
# 누적 합 구하는 거는 꼭 초기화하는 변수 만들기!!!
for i in range(10):
    sum_val += int(arr[i])
print(sum_val)

arr = [1, 2]

for elem in arr:
    print(elem)

arr = list(map(int, input().split()))
print(arr)

'''

arr = list(map(int, input().split()))

sum_val = 0
for i in arr:
    sum_val += i
print(sum_val)