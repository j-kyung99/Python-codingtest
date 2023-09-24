def solution(a, b):
    ab = int(str(a)+str(b))
    abab = 2 * a * b
    return max(ab, abab)