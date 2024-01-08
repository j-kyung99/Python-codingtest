def solution(elements):
    element = elements * 2
    arr = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            arr.add(sum(element[i:i+j+1]))
    return len(arr)