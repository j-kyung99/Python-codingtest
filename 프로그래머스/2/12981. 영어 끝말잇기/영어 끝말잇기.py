def solution(n, words):
    arr = [words[0]]
    for i in range(1, len(words)):
        idx = i % n + 1
        fail = i // n + 1
        if words[i] in arr or words[i][0] != words[i-1][-1]:
            return [idx, fail]
        else:
            arr.append(words[i])
    return [0, 0]