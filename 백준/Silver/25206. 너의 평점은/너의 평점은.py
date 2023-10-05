import sys

dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

Sum = 0
mulSum = 0
average = 0

for i in range(20):
    arr = sys.stdin.readline().strip().split()
    if arr[2] != "P":
        grade = float(arr[1])
        Sum += grade
        mulSum += grade * dic[arr[2]]
print(mulSum / Sum)
