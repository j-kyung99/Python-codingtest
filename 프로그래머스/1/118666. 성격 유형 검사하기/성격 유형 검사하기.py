def solution(survey, choices):
    category = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    arr = [0] * 8
    answer = '';
    for i in range(len(choices)):
        if 0 < choices[i] < 4:
            arr[category.index(survey[i][0])] += 4-choices[i]
        elif 4 < choices[i] < 8:
            arr[category.index(survey[i][1])] += choices[i] - 4
    for i in range(len(category)//2):
        if (arr[i*2]) >= (arr[i*2+1]):
            answer += category[i*2]
        else:
            answer += category[i*2+1]
    return answer