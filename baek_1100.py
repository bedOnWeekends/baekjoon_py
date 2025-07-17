cnt = 0
for i in range(8):
    line = input()
    for j, char in enumerate(line):
        if char == 'F':
            if i % 2 and j % 2:
                cnt += 1
            elif i % 2 == 0 and j % 2 == 0:
                cnt += 1
print(cnt)


