n, b = tuple(map(int,input().split()))

digits = []

while n > 1:
    digits.append(n % b)
    n //= b

digits.append(n)

for digit in digits[::-1]:
    print(digit, end='')