def solution(array, commands):
    answer = []
    for idx in commands:
        arr = array[idx[0]-1:idx[1]]
        print(arr)
        arr.sort()
        answer.append(arr[idx[2]-1])
    return answer