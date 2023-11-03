def solution(d, budget):
    answer = 0
    money = 0
    d.sort()
    for i in d:
        if money < budget:
            money += i
            answer += 1
            if money > budget:
                money -= i
                answer -= 1
            elif money == budget:
                return answer
            else:
                pass
    return answer