def solution(k, score):
    answer = []
    scores = []
    for i in range(len(score)):
        scores.append(score[i])
        scores.sort(reverse=True)
        if len(scores) == k+1:
            scores = scores[:k]
        answer.append(min(scores))
    return answer