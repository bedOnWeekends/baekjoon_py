N = int(input())
max_point = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    arr1 = arr[0:2]
    arr2 = arr[2:7]
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    point = arr1[0] + arr2[0] + arr2[1]
    max_point = max(max_point, point)

print(max_point)

