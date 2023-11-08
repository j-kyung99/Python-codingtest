def solution(a, b, n):
    answer = 0
    while n >= a:
        k = (n // a) * b
        answer += k
        n = n % a + k
    return answer