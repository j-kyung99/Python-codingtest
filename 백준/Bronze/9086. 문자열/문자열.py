import sys

T = int(sys.stdin.readline())
for i in range(T):
    answer = ""
    str = sys.stdin.readline().strip()
    answer = str[0] + str[-1]
    print(answer)
