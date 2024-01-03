def solution(k, tangerine):
    answer, count = 0, 0
    dic = {}
    arr = set(tangerine)
    for i in list(set(tangerine)):
        dic[i]=0
    for i in tangerine:
        dic[i]+=1
    sort = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    for i in sort:
        answer += sort[i]
        count += 1
        if answer >= k:
            break
    return count