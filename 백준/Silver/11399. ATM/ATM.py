import sys

n = int(sys.stdin.readline())
atm = list(map(int, sys.stdin.readline().split()))
atm.sort()

answer = 0

time = 0

for i in atm:
    answer += time + i
    time += i

print(answer)
