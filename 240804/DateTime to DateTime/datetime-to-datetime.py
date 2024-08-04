a, b, c = tuple(map(int, input().split()))

date, hour, mins = 11, 11, 11
elapsed_time = 0

if a < 11:
    print(-1)

else:
    for i in range(10000):
        if date == a and hour == b and mins == c:
            break
        elapsed_time += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0

        if hour == 24:
            date += 1
            hour = 0
    print(elapsed_time)