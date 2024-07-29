date = input()

arr = date.split('-')

yyy = int(arr[2])
mm = int(arr[0])
dd = int(arr[1])

print(f'{yyy}.{mm}.{dd}')