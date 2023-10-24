import sys

n = int(sys.stdin.readline())

station = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

money = 0
minPrice = price[0]
for i in range(n - 1):
    if price[i] < minPrice:
        minPrice = price[i]
    money += minPrice * station[i]

print(money)
