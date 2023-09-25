def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        num = []
        for i in range(len(arr)):
            if i >= s and i <= e and arr[i] > k:
                num.append(arr[i])
        if len(num) == 0:
            answer.append(-1)
        else:
            answer.append(min(num))
            
    return answer