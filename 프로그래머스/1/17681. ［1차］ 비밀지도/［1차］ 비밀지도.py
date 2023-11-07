def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        s = ''
        num = arr1[i] | arr2[i]
        for j in range(n):
            if num % 2 == 0:
                s = ' ' + s
            else:
                s = '#' + s
            num = int(num/2)
        answer.append(s)
    return answer