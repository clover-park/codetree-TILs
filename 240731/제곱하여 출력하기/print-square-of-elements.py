# [(append 안에 들어갈 내용) (for loop) <조건문>]
count = int(input())
arr = list(map(int, input().split()))

new_arr = [i**2 for i in arr]

for i in range(count):
	print(new_arr[i], end=" ")