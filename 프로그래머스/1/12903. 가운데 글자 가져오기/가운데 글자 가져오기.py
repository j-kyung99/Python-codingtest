def solution(s):
    n = len(s)//2
    if len(s)%2 == 1:
        return s[n]
    else:
        return s[n-1] + s[n]