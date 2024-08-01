code, color, second = tuple(input().split())

class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self. color = color
        self.second = second

a = Bomb(code, color, second)

print(f'code : {a.code}')
print(f'color : {a.color}')
print(f'second : {a.second}')