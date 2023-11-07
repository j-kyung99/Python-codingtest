def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        food[i] = int(food[i] / 2)
    for i in range(1, len(food)):
        for j in range(food[i]):
            answer += str(i)
    answer += '0'
    for i in range(len(food) - 1, 0, -1):
        for j in range(food[i]):
            answer += str(i)
    return answer