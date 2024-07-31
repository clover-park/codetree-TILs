arr = list(map(int, input().split()))

smaller_than_fivehunnid = 0
bigger_than_fivehunnid = 1000

for i in arr:
    if i > 500:
        if i < bigger_than_fivehunnid:
            bigger_than_fivehunnid = i
    elif i < 500:
        if i > smaller_than_fivehunnid:
            smaller_than_fivehunnid = i

print(smaller_than_fivehunnid, bigger_than_fivehunnid)