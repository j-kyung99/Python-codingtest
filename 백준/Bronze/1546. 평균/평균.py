import sys

n = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))

m = max(score)

for i in range(len(score)):
    score[i] = score[i] / m * 100
s = sum(score) / len(score)
print(s)
