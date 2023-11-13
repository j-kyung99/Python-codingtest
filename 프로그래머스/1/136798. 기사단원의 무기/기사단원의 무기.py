def factor(n, limit, power):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            count += 1
            if i**2 != n:
                count += 1
    return power if count > limit else count

def solution(number, limit, power):
    arr = []
    for i in range(1, number+1):
        arr.append(factor(i, limit, power))
    return sum(arr)