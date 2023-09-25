def solution(a, d, included):
    s = 0
    num = 0
    for i in range(len(included)):
        if i == 0:
            num += a
            if included[i] == True:
                s += num
                num += d
            else:
                num += d
        else:
            if included[i] == True:
                s += num
                num += d
            else:
                num += d
    return s