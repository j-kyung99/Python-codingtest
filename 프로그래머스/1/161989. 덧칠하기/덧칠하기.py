def solution(n, m, section):
    answer = 0
    arr = [1] * (n+1)
    for i in section:
        arr[i] = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            answer += 1
            for j in range(i, i+m):
                if j >= len(arr):
                    continue
                arr[j] = 1
    return answer