import sys

count = 1

while True:
    L, P, V = map(int, sys.stdin.readline().split())
    result = 0
    if L == P == V == 0:
        break
    result += (V // P) * L
    V = V % P
    if L < V:
        result += L
    else:
        result += V
    print(f"Case {count}: {result}")
    count += 1
