arr = [-1] * 26
str = input()
for i in range(len(str)):
    idx = ord(str[i]) - 97
    if arr[idx] == -1:
        arr[idx] = i
print(*arr)
