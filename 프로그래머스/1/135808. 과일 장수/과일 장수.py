def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    arr = []
    for i in range(len(score)):
        if len(arr) < m:
            arr.append(score[i])
        if len(arr) == m:
            answer += min(arr) * m
            arr.clear()
    return answer