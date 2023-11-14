def solution(N, stages):
    answer = {}
    challenge = len(stages)
    for i in range(1, N+1):
        if challenge != 0:
            count = stages.count(i)
            answer[i] = count / challenge
            challenge -= count
        else:
            answer[i] = 0
    return sorted(answer, key = lambda x: answer[x], reverse=True)