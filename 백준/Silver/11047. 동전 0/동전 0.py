import sys

N, K = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)

count = 0

for i in arr:
    count += K // i
    K = K % i
print(count)
