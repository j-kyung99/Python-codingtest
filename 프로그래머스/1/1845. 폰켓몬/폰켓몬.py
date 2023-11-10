def solution(nums):
    num = set(nums)
    return len(num) if len(nums)/2 >= len(num) else len(nums)/2