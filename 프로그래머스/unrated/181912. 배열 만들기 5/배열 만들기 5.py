def solution(intStrs, k, s, l):
    answer = []
    for idx in intStrs:
        num = int(idx[s:s+l])
        if num > k:
            answer.append(num)
    return answer