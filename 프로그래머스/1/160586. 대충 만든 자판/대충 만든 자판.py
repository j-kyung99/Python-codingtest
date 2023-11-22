def solution(keymap, targets):
    answer = []
    for target in targets:
        counts = 0
        
        for idx in target:
            flag = False
            count = 101
            for key in keymap:
                if idx in key:
                    count = min(key.index(idx)+1, count)
                    flag = True
            if not flag:
                counts = -1
                break
            counts += count
        answer.append(counts)
    return answer