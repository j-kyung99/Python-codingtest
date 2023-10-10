import sys
import itertools

stats = []

for _ in range(9):
    stat = int(sys.stdin.readline().strip())
    stats.append(stat)

for i in itertools.combinations(stats, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
