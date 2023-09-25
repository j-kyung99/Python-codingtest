import math
def solution(n):
    s = 0
    if n%2 == 1:
        return sum(range(1, n+1, 2))
    else:
        for i in range(0, n+1, 2):
            s += pow(i, 2)
        return s