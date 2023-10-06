import sys

n, m = list(map(int, sys.stdin.readline().split()))

answer = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    answer.append(a)

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        answer[i][j] += a[j]
for row in answer:
    print(*row)
