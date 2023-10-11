import sys

answer = ""

maxNum = 0

arr = []

while 1:
    char = sys.stdin.readline().strip()
    if len(char) == 0:
        break
    if len(char) > maxNum:
        maxNum = len(char)
    arr.append(char)

for i in range(maxNum):
    for j in range(len(arr)):
        if len(arr[j]) < i + 1:
            pass
        else:
            answer += arr[j][i]
print(answer)
