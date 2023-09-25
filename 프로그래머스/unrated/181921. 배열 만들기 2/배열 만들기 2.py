def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
    return [-1] if len(answer) == 0 else answer