import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

for i in range(n):
    arr.append(i + 1)
for idx in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    arr = arr[:i] + arr[i : j + 1][::-1] + arr[j + 1 :]
print(*arr)
