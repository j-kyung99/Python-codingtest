def solution(n):
    nCount = bin(n)[2:].count('1')
    for i in range(n+1, 1000001):
        iCount = bin(i)[2:].count('1')
        if nCount == iCount:
            return i