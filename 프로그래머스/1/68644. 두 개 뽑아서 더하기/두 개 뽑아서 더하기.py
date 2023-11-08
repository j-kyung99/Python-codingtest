from itertools import combinations

def solution(numbers):
    answer = []
    com = list(combinations(numbers, 2))
    for i in com:
        answer.append(i[0] + i[1])
    answer = list(set(answer))
    answer.sort()
    return answer