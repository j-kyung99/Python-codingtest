def solution(n):
    temp = []
    answer = 0
    while n:
        temp.append(n % 3)
        n = n // 3
    mul = 1
    temp.reverse()
    for i in temp:
        answer += i * mul
        mul *= 3
    return answer