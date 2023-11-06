def solution(s, n):
    answer = ''
    for i in s:
        c = ord(i)
        if ord('A') <= c <= ord('Z'):
            c += n
            if c > ord('Z'):
                c -= 26
        if ord('a') <= c <= ord('z'):
            c += n
            if c > ord('z'):
                c -= 26
        answer += chr(c)
    return answer