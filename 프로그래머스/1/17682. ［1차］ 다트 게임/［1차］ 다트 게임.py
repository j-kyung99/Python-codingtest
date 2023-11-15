def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')
    answer = []
    count = 0
    for idx in dartResult:
        if idx.isnumeric():
            count += int(idx)
            continue
        elif idx == 'A':
            count += 10
            continue
        elif idx == 'S':
            answer.append(count)
        elif idx == 'D':
            answer.append(count ** 2)
        elif idx == 'T':
            answer.append(count ** 3)
        elif idx == '*':
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2
        elif idx == '#':
            answer[-1] *= -1
        count = 0
    return(sum(answer))
            