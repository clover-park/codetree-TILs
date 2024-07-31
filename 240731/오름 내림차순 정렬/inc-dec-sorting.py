'''
오름차순
arr.sort()
arr = sorted(arr)

내림차순
arr.sort(reverse = True)
오름차순으로 만든 뒤 슬라이싱 [::-1]
arr = list(reversed(arr))
'''

n = int(input())

arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

for i in range(n):
    print(sorted_arr[i], end=' ')
print()
reversed_arr = sorted_arr[::-1]

for i in range(n):
    print(reversed_arr[i], end=' ')