def solution(s):
    answer = True
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False