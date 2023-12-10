def solution(s):
    answer = []
    arr = s.split(' ')
    for word in arr:
        answer.append(word.capitalize())
    return ' '.join(answer)