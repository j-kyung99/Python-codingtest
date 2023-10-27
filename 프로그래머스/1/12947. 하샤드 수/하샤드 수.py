def solution(x):
    arr = list(map(int, str(x)))
    num = sum(arr)
    if x % num == 0:
        return True
    else:
        return False