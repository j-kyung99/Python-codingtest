def solution(answers):
    result = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if answer == one[idx%len(one)]:
            score[0] += 1
        if answer == two[idx%len(two)]:
            score[1] += 1
        if answer == three[idx%len(three)]:
            score[2] += 1
    for idx, student in enumerate(score):
        if student == max(score):
            result.append(idx+1)
    return result