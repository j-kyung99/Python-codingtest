fibo = [0] * 100001
fibo[1] = 1
for i in range(2, 100001):
    fibo[i] = fibo[i-2] + fibo[i-1]
def solution(n):
    return fibo[n] % 1234567