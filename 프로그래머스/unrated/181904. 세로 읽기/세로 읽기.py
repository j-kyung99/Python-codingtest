def solution(my_string, m, c):
    answer = ''
    num = c-1
    while(num < len(my_string)):
        answer += my_string[num]
        num += m
    return answer