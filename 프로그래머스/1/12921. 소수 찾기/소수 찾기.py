def decimal(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if decimal(i):
            answer += 1
    return answer