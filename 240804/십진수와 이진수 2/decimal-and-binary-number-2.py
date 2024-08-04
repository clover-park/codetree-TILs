n = list(input())

binary = list(map(int, n))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]

num *= 17

digits = []

while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit, end='')