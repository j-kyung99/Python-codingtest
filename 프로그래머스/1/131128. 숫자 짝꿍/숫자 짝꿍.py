from collections import Counter

def solution(X, Y):
    answer = ''
    counter1 = Counter(X)
    counter2 = Counter(Y)
    common = sorted(list((counter1 & counter2).elements()), reverse=True)
    if set(common) == {'0'}:
        return "0"
    answer = ''.join(common)
    if answer == '':
        return "-1"
    else:
        return answer