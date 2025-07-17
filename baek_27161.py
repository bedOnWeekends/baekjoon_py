N = int(input())
ans_time = 1
time_reverse = False

def time_tick(tr, t):
    if tr:
        t -= 1
    else:
        t += 1

    if t < 1:
        t += 12
    elif t > 12:
        t -= 12

    return t

for i in range(N):
    watch, time = map(str, input().split())
    time = int(time)
    say = ""
    if watch == "HOURGLASS" and time == ans_time:
        say = " NO"
    elif watch == "HOURGLASS":
        say = " NO"
        time_reverse = not time_reverse
    elif time == ans_time:
        say = " YES"
    else:
        say = " NO"

    print(ans_time.__str__() + say)
    ans_time = time_tick(time_reverse, ans_time)












