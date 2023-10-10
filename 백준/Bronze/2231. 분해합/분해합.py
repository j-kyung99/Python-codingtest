import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    answer = sum(map(int, str(i)))
    answer += i

    if answer == N:
        print(i)
        break
    if i == N:
        print(0)
