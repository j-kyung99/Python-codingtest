def solution(s, skip, index):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in skip:
        alpha.remove(x)
    for idx in s:
        change = alpha.index(idx) + index
        while change >= len(alpha):
            change -= len(alpha)
        answer += alpha[change]
    return answer