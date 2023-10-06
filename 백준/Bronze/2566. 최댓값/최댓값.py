import sys

answer = []

for i in range(9):
    num = list(map(int, sys.stdin.readline().split()))
    maxNum = max(num)
    answer.append([maxNum, i + 1, num.index(maxNum) + 1])

max_value = answer[0][0]
max_array = answer[0]
for i in answer:
    if i[0] > max_value:
        max_value = i[0]
        max_array = i
print(f"{max_value}\n{max_array[1]} {max_array[2]}")
