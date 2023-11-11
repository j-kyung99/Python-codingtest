from itertools import combinations

def decimal(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for i in comb:
        answer += decimal(sum(i))
    
    return answer