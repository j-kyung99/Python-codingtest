def solution(num_list):
    a, b = 1, 0
    for i in num_list:
        a *= i
        b += i
    return 1 if a < b**2 else 0