import re

def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for s in babbling:
        for c in can:
            if c * 2 not in s:
                s = s.replace(c, ' ')
        if s.isspace():
            answer += 1
    return answer