import sys

data = [int(sys.stdin.readline().strip()) for i in range(9)]
print(f"{max(data)}\n{data.index(max(data))+1}")
