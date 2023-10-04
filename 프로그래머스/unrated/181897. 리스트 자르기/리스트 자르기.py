def solution(n, slicer, num_list):
    a, b, c = slicer
    b += 1
    if n == 1:
        return num_list[0:b]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b]
    else:
        return num_list[a:b:c]