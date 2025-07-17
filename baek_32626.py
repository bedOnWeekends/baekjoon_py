s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())
p_x, p_y = map(int, input().split())

if s_x != e_x and s_y != e_y:
    print(1)
elif s_x == e_x:
    if p_x == s_x and min(s_y, e_y) < p_y < max(s_y, e_y):
        print(2)
    else:
        print(0)
elif s_y == e_y:
    if p_y == s_y and min(s_x, e_x) < p_x < max(s_x, e_x):
        print(2)
    else:
        print(0)
