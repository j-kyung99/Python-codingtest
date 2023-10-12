import sys

arr = [[0 for _ in range(101)] for _ in range(101)]
n = int(sys.stdin.readline())

for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            arr[i][j] = 1

answer = 0

for i in arr:
    answer += i.count(1)
print(answer)
