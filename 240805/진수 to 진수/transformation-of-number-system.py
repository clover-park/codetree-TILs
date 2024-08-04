a, b = tuple(map(int, input().split()))

n = list(input())
n = list(map(int, n))
num = 0

for i in range(len(n)):
    num = num * a + n[i]

binary = []

while True:
    if num < b:
        binary.append(num)
        break
    binary.append(num % b)
    num //= b

for digit in binary[::-1]:
    print(digit, end='')