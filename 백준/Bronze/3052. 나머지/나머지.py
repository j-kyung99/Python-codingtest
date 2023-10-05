import sys

arr = []

for i in range(10):
    num = int(sys.stdin.readline())
    arr.append(num % 42)
arr = set(arr)
print(len(arr))
