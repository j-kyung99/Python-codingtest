def solution(numbers, hand):
    answer = ''
    nowL, nowR = 10, 12
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            nowL = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            nowR = number
        else:
            if number == 0:
                number = 11
            disL = abs(nowL - number)//3+ abs(nowL - number)%3
            disR = abs(nowR - number)//3+ abs(nowR - number)%3
            if disL > disR:
                answer += 'R'
                nowR = number
            elif disR > disL:
                answer += 'L'
                nowL = number
            else:
                if hand == 'left':
                    answer += 'L'
                    nowL = number
                else:
                    answer += 'R'
                    nowR = number
    return answer