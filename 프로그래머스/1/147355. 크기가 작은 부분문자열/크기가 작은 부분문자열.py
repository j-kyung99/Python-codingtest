def solution(t, p):
    answer = 0
    arr = []
    for i in range(len(t)):
        if len(t[i:i+len(p)]) < len(p):
            pass
        else:
            arr.append(int(t[i:i + len(p)]))
    for i in arr:
        if i <= int(p):
            answer += 1
    return answer