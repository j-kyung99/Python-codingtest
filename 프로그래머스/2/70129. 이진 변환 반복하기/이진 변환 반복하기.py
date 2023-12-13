def solution(s):
    total, count = 0, 0
    while(1):
        if s == '1':
            break
        total += 1
        count += len([i for i in s if i == '0'])
        s = len([i for i in s if i == '1'])
        s = bin(s)[2:]
    return [total, count]
        
        