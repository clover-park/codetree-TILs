class User:
    def __init__(self, id, lev):
        self.id = id
        self.lev = lev

User1 = User('codetree', '10')
User2 = User('codetree', '10')

id, lev = tuple(input().split())
User2.id = id
User2.lev = lev

print(f'user {User1.id} lv {User1.lev}')
print(f'user {User2.id} lv {User2.lev}')