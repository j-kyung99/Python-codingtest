def solution(name, yearning, photo):
    answer = []
    dic = {}

    for i in range(len(name)):
        dic.update({name[i]: yearning[i]})
    for i in photo:
        print(i)
        count = 0
        for j in i:
            print(j)
            if j in dic:
                count += dic[j]
        answer.append(count)
    return answer