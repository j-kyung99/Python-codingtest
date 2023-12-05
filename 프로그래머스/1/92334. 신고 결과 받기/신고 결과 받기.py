def solution(id_list, report, k):
    report = set(report)
    answer = [0] * len(id_list)
    arr = {i: 0 for i in id_list}
    for i in report:
        a, b = i.split(' ')
        arr[b] += 1
    for i in report:
        a, b = i.split(' ')
        if arr[b] >= k:
            answer[id_list.index(a)] += 1
    return answer