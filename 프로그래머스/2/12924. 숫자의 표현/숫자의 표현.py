def solution(n):
    answer = 0
    for i in range(1, n+1):
        ssum = 0
        while ssum < n:
            ssum += i
            i += 1
        if ssum == n:
            answer += 1
    return answer