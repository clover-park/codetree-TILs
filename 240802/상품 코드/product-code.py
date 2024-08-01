product, code = tuple(input().split())

class Shop:
    def __init__(self, product = 'codetree', code = 50):
        self.product = product
        self.code = code

a = Shop()
b = Shop(product, code)

print(f'product {a.code} is {a.product}')
print(f'product {b.code} is {b.product}')