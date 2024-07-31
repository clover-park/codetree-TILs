arr_2d = [
    list(input().split())
    for _ in range(5)
]
for i in range(5):
    for j in range(3):
        arr_2d[i][j]= chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
        print(arr_2d[i][j], end=' ')
    print()

"""
i/j  0 1 2
0    a b c
1    d e f
2    g h i
3    j k l
4    m n o
"""