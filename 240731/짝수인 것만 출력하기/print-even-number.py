count = int(input())
arr = map(int, input().split())
even_num = []

for elem in arr:
	if elem % 2 == 0:
		even_num.append(elem)
for i in even_num:
    print(i, end=' ')
'''
arr = list(map(int, input().split()))
sum_val = 0 -> sum 변수 만들 수도 있다.
cnt = 0

for elem in arr:
	if elem == 0:
		break -> break 문을 먼저 쓰면 된다.
	if elem % 2 == 0:
		sum_val += elem
		cnt += 1

print(cnt, sum_val)
'''