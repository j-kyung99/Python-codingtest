def solution(numbers):
    all = sum([i for i in range(0,10)])
    for i in numbers:
        all -= i
    return all