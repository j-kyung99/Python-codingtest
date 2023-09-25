def solution(n):
    i = n
    answer = []
    while(i != 1):
        answer.append(i)
        if i%2 == 0:
            i /= 2
        else:
            i = 3*i+1
    answer.append(1)
    return answer