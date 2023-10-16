import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

last = 0
count = 0

for i, j in arr:
    if i >= last:
        count += 1
        last = j

print(count)
