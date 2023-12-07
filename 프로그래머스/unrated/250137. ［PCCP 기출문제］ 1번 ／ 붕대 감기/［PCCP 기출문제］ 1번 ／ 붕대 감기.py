def solution(bandage, health, attacks):
    answer = health
    time, sec, plus = bandage
    attacks_dic = {attack[0]: attack[1] for attack in attacks}
    max_time = attacks[-1][0]
    con = 0
    for i in range(1, max_time + 1):
        if i in attacks_dic:
            answer -= attacks_dic[i]
            con = 0
            if answer <= 0:
                return -1
        else:
            con += 1
            if con >= time:
                answer += sec + plus
                con = 0
            else:
                answer += sec
            
            if answer > health:
                answer = health
        
    return answer