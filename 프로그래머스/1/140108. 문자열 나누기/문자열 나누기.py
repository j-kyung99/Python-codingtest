def solution(s):
    answer = 0
    yes = 0
    no = 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            yes += 1
        else:
            no += 1
        if yes == no:
            answer += 1
            if i+1 < len(s):
                x = s[i+1]
        if yes != no:
            if i == len(s) - 1:
                answer += 1
    return answer