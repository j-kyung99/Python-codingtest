import sys

arr = [0 for _ in range(1001)]

N, L = map(int, sys.stdin.readline().split())

tape = list(map(int, sys.stdin.readline().split()))
tape.sort()

count = 0

for i in tape:
    if arr[i] == 1:
        continue
    for j in range(L):
        if i + j > 1000:
            break
        arr[i + j] = 1
    count += 1
print(count)
