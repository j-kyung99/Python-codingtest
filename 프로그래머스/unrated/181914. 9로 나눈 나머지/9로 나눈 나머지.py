def solution(number):
    number = int(number)
    while(number > 8):
        number = number%9
    return number