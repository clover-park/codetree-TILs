# 초기값 세팅이 중요하다.

arr = list(map(int, input().split()))

# 초기값 세팅하기
max_val = 0

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)