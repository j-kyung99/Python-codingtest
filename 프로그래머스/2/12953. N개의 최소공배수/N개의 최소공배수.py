def solution(arr):
    m = max(arr)
    while(True):
        count = 0
        for i in arr:
            if m % i == 0:
                count += 1
            else:
                m += 1
                break
        if count == len(arr):
            return m