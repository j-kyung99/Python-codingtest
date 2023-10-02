def solution(my_string):
    result = [0] * 52
    for char in my_string:
        if char.isupper():
            result[ord(char)-65] += 1
        else:
            result[ord(char)-97+26] += 1
    return result