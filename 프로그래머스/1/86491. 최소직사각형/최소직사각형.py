def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    data = sorted(sizes, key=lambda x:x[0], reverse=True)
    w = data[0][0]
    data = sorted(sizes, key=lambda x:x[1], reverse=True)
    h = data[0][1]
    return w*h