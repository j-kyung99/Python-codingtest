def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = len([x for x in lottos if x == 0])
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                count += 1
    print(f'count : {count}, zero : {zero}')
    if 7 - (count + zero) == 7 or 7 - (count + zero) == 6:
        answer.append(6)
    else:
        answer.append(7 - (count + zero))
    if count == 0 or count == 1:
        answer.append(6)
    else:
        answer.append(7 - count)
    return answer