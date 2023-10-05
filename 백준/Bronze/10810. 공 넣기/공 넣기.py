n, m = map(int, input().split())
arr = [0] * n
for idx in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    for idx2 in range(i, j + 1):
        arr[idx2] = k
print(*arr)
