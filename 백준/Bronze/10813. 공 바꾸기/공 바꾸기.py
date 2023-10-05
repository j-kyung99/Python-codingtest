import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for idx in range(n):
    arr.append(idx + 1)
for idx in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    arr[i], arr[j] = arr[j], arr[i]
print(*arr)