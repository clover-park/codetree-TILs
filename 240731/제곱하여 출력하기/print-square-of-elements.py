# [(append 안에 들어갈 내용) (for loop) <조건문>]
count = int(input())
arr = list(map(int, input().split()))

new_arr = [i**2 for i in arr]

print(new_arr[0],new_arr[1],new_arr[2])