'''
문자열 정렬은 알파벳을 리스트로 만든 후
''.join(arr)으로 붙여서 문자열로 만든다.
'''

s = input()

s = list(s)
s.sort()
s=''.join(s)
print(s)