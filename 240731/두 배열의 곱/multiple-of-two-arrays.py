matrix1 = [list(map(int, input().split()))
    for _ in range(3)]


space = list(map(int, input().split()))

matrix2 = [list(map(int, input().split()))
    for _ in range(3)]


result = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] * matrix2[i][j]

for i in range(3):
    for j in range(3):
        print(result[i][j], end = ' ')
    print()