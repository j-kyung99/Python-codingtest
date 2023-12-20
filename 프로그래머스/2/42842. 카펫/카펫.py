def solution(brown, yellow):
    carpet = brown + yellow
    for b in range(1, carpet+1):
        a = carpet / b
        if a % 1 == 0 and a >= b and 2*a + 2*b - 4 == brown:
            return [a, b]