import sys


N = int(sys.stdin.readline())
answer = 0
for i in range(N):
    answer += int(sys.stdin.read(1))
print(answer)
